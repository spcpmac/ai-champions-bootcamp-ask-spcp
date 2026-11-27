"""Parsing + chunking of GitBook llms-full.txt exports, tickets, Slack threads and the OpenAPI spec.

Pure functions (no network), so they can be unit-tested and reused by the app.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field

from functools import lru_cache

from core.config import CHUNK_OVERLAP_TOKENS, CHUNK_TOKENS



@lru_cache(maxsize=1)
def _enc():
    import tiktoken  # lazy: only needed at ingestion time

    return tiktoken.get_encoding("cl100k_base")

ERROR_CODE_RE = re.compile(
    r"\b(invalid_[a-z_]+|unauthorized_client|access_denied|server_error|temporarily_unavailable|"
    r"unsupported_[a-z_]+|use_dpop_nonce|login_required|consent_required|expired_token|"
    r"authorization_pending|slow_down)\b"
)


def ntokens(text: str) -> int:
    return len(_enc().encode(text, disallowed_special=()))


@dataclass
class Chunk:
    text: str
    metadata: dict = field(default_factory=dict)

    @property
    def id(self) -> str:
        key = f"{self.metadata.get('domain')}|{self.metadata.get('source_type')}|" \
              f"{self.metadata.get('source_id', '')}|{self.text}"
        return hashlib.sha1(key.encode()).hexdigest()[:20]


# --------------------------------------------------------------------------- cleaning

def _cell_to_md(cell) -> str:
    from markdownify import markdownify

    md = markdownify(cell.decode_contents(), heading_style="ATX", bullets="-",
                    escape_underscores=False, escape_asterisks=False, escape_misc=False)
    md = re.sub(r"\s*\n\s*", " ", md).strip()
    return md.replace("|", "\\|")


def html_table_to_md(html: str) -> str:
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for tr in soup.find_all("tr"):
        cells = [_cell_to_md(c) for c in tr.find_all(["th", "td"])]
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    lines = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * width]
    lines += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(lines)


def clean_markdown(text: str) -> str:
    """Normalise GitBook markdown: HTML tables → markdown, strip noise tags."""
    text = re.sub(r"<table[\s\S]*?</table>", lambda m: "\n\n" + html_table_to_md(m.group(0)) + "\n\n", text)
    text = re.sub(r"<summary>([\s\S]*?)</summary>", r"**\1**", text)
    text = re.sub(r"</?(details|mark|figure|figcaption|div|span|picture|br)\b[^>]*>", "", text)
    text = re.sub(r"<img\b[^>]*>", "", text)
    text = re.sub(r'<a href="#[^"]*" id="[^"]*"></a>', "", text)
    text = re.sub(r"<a [^>]*>([\s\S]*?)</a>", r"\1", text)
    text = re.sub(r"\{%\s*[^%]*%\}", "", text)             # GitBook hint/tab blocks
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)         # markdown images
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# --------------------------------------------------------------------------- GitBook parsing

def _iter_lines_with_fence(text: str):
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            yield line, True
            continue
        yield line, in_fence


def parse_index(llms_txt: str) -> list[tuple[str, str]]:
    """Parse GitBook llms.txt → ordered [(title, url)]."""
    out = []
    for m in re.finditer(r"^\s*[-*] \[([^\]]+)\]\((https?://[^)]+)\)", llms_txt, re.M):
        url = m.group(2)
        out.append((m.group(1).strip(), url[:-3] if url.endswith(".md") else url))
    return out


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def split_gitbook_pages(text: str, index: list[tuple[str, str]] | None = None,
                        default_url: str = "") -> list[dict]:
    """Split an llms-full.txt export into pages at H1 headings (ignoring code fences)."""
    pages: list[dict] = []
    cur_title, cur_lines = None, []
    for line, fenced in _iter_lines_with_fence(text):
        if not fenced and re.match(r"^# \S", line):
            if cur_title is not None:
                pages.append({"title": cur_title, "body": "\n".join(cur_lines)})
            cur_title, cur_lines = line[2:].strip(), []
        elif cur_title is not None:
            cur_lines.append(line)
    if cur_title is not None:
        pages.append({"title": cur_title, "body": "\n".join(cur_lines)})

    # Drop LLM-directed preamble pages and nav footers.
    pages = [p for p in pages if _norm(p["title"]) != "agentinstructions"]
    for p in pages:
        p["body"] = re.sub(r"^\[(Next|Previous) Page\]\([^)]*\)\s*$", "", p["body"], flags=re.M)
        p["body"] = re.sub(r"^>\s*(This is part|The content is paginated|Next part|Previous part|"
                           r"Page index|Agents can also).*$", "", p["body"], flags=re.M)
        p["body"] = re.sub(r"^---\s*$", "", p["body"], flags=re.M)

    # Map pages to URLs by walking the ordered page index.
    ptr = 0
    for p in pages:
        p["url"] = default_url
        if not index:
            continue
        for j in range(ptr, min(ptr + 25, len(index))):
            if _norm(index[j][0]) == _norm(p["title"]):
                p["url"], ptr = index[j][1], j + 1
                break
    return pages


# --------------------------------------------------------------------------- chunking

def _blocks(body: str) -> list[tuple[str, str, int]]:
    """Split a page body into atomic blocks: (kind, text, heading_level)."""
    blocks: list[tuple[str, str, int]] = []
    buf: list[str] = []
    kind = "para"

    def flush():
        nonlocal buf, kind
        t = "\n".join(buf).strip()
        if t:
            blocks.append((kind, t, 0))
        buf, kind = [], "para"

    in_fence = False
    for line in body.splitlines():
        if line.lstrip().startswith("```"):
            if not in_fence:
                flush()
                kind = "code"
                in_fence = True
                buf.append(line)
            else:
                buf.append(line)
                in_fence = False
                flush()
            continue
        if in_fence:
            buf.append(line)
            continue
        h = re.match(r"^(#{2,6}) (.+)", line)
        if h:
            flush()
            blocks.append(("heading", h.group(2).strip(), len(h.group(1))))
            continue
        is_table = line.lstrip().startswith("|")
        if is_table and kind != "table":
            flush()
            kind = "table"
        elif not is_table and kind == "table":
            flush()
        if not line.strip() and kind != "table":
            flush()
            continue
        buf.append(line)
    flush()
    return blocks


def _split_oversized(kind: str, text: str, limit: int) -> list[str]:
    if ntokens(text) <= limit:
        return [text]
    lines = text.splitlines()
    if kind == "table" and len(lines) > 2:
        header, rows = lines[:2], lines[2:]
        parts, cur = [], []
        for r in rows:
            if cur and ntokens("\n".join(header + cur + [r])) > limit:
                parts.append("\n".join(header + cur))
                cur = []
            cur.append(r)
        if cur:
            parts.append("\n".join(header + cur))
        # A single huge row still needs hard splitting
        return [s for p in parts for s in (_hard_split(p, limit) if ntokens(p) > limit else [p])]
    return _hard_split(text, limit)


def _hard_split(text: str, limit: int) -> list[str]:
    toks = _enc().encode(text, disallowed_special=())
    return [_enc().decode(toks[i : i + limit]) for i in range(0, len(toks), limit)]


_SKIP_SEGMENTS = {"docs", "singpass-developer-docs", "technical-specifications", "products", "introduction"}


def url_parents(url: str, depth: int = 2) -> str:
    """Human-readable parent sections from a doc URL, e.g. '.../migration-guides/myinfo-v3-apps'
    → 'Migration Guides'. Gives chunks their place in the docs hierarchy (helps retrieval)."""
    path = re.sub(r"^https?://[^/]+/", "", url).strip("/").split("/")[:-1]
    segs = [p for p in path if p and p not in _SKIP_SEGMENTS]
    legacy = [p for p in segs if p.startswith("legacy")][:1]   # always keep the "Legacy …" marker
    segs = legacy + [p for p in segs[-depth:] if p not in legacy]

    def nice(seg: str) -> str:
        t = seg.replace("-", " ").title()
        for a, b in (("V3 V4", "v3/v4"), ("Api", "API"), ("Fapi", "FAPI"), ("Pre ", "Pre-"), ("Cdp", "CDP"),
                     ("Sdp", "SDP"), ("Oidc", "OIDC"), ("Ciba", "CIBA")):
            t = t.replace(a, b)
        return t

    return " > ".join(nice(p) for p in segs)


def chunk_page(page: dict, base_meta: dict, limit: int = CHUNK_TOKENS,
               overlap: int = CHUNK_OVERLAP_TOKENS) -> list[Chunk]:
    body = clean_markdown(page["body"])
    title = page["title"]
    parents = url_parents(page.get("url", ""))
    chunks: list[Chunk] = []
    section = ""
    cur: list[tuple[str, str]] = []   # (kind, text)
    cur_section = ""

    def emit(carry_overlap: bool):
        nonlocal cur
        if not cur or all(k == "heading" for k, _ in cur):
            return
        crumb = f"{title} > {cur_section}" if cur_section else title
        if parents:
            crumb = f"{parents} > {crumb}"
        text = f"[{crumb}]\n" + "\n\n".join(t for _, t in cur)
        meta = dict(base_meta, title=title, section=cur_section or title, url=page.get("url", ""),
                    error_codes=",".join(sorted(set(ERROR_CODE_RE.findall(text)))))
        chunks.append(Chunk(text, meta))
        if carry_overlap:
            tail, acc = [], 0
            for k, t in reversed(cur):
                n = ntokens(t)
                if k in ("table", "code") or acc + n > overlap:
                    break
                tail.insert(0, (k, t))
                acc += n
            cur = tail
        else:
            cur = []

    for kind, text, level in _blocks(body):
        if kind == "heading":
            hashes = "#" * level
            if level == 2:
                section = text
                if cur and ntokens("\n\n".join(t for _, t in cur)) >= 200:
                    emit(carry_overlap=False)
            if not cur:
                cur_section = section
            cur.append(("heading", f"{hashes} {text}"))
            continue
        for piece in _split_oversized(kind, text, limit - 60):
            size = ntokens("\n\n".join(t for _, t in cur)) + ntokens(piece)
            if cur and size > limit:
                emit(carry_overlap=True)
                cur_section = section
            if not cur:
                cur_section = section
            cur.append((kind, piece))
    emit(carry_overlap=False)
    return chunks


# --------------------------------------------------------------------------- other sources

def ticket_to_chunk(t: dict, domain: str) -> Chunk:
    text = (
        f"[Support ticket {t['id']} — {t['product']}] {t['subject']}\n"
        f"Category: {t['category']} | Environment: {t['environment']} | "
        f"Error code: {t.get('error_code') or 'n/a'} | Flow step: {t.get('flow_step', 'n/a')}\n\n"
        f"Problem reported:\n{t['description']}\n\nResolution:\n{t['resolution']}"
    )
    meta = {"domain": domain, "source_type": "ticket", "source_id": t["id"], "title": t["subject"],
            "section": t["category"], "product": t["product"], "url": "",
            "error_codes": t.get("error_code") or "", "synthetic": True}
    return Chunk(text, meta)


def slack_to_chunk(th: dict, domain: str) -> Chunk:
    msgs = "\n".join(f"- {m['role']}: {m['text']}" for m in th["messages"])
    text = (f"[Slack #{th['channel']} thread {th['id']} — {th['product']}] {th['topic']}\n\n"
            f"{msgs}\n\nOutcome: {th['outcome']}")
    meta = {"domain": domain, "source_type": "slack", "source_id": th["id"], "title": th["topic"],
            "section": th["channel"], "product": th["product"], "url": "",
            "error_codes": ",".join(sorted(set(ERROR_CODE_RE.findall(text)))), "synthetic": True}
    return Chunk(text, meta)


def _flatten_fields(schema: dict, prefix: str = "", depth: int = 0) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    if depth > 4 or not isinstance(schema, dict):
        return out
    parts = [schema] + [s for s in schema.get("allOf", []) if isinstance(s, dict)]
    if schema.get("type") == "array" and isinstance(schema.get("items"), dict):
        parts.append(schema["items"])
    for part in parts:
        if part is not schema and part.get("allOf"):
            out += _flatten_fields(part, prefix, depth + 1)
        for name, sub in (part.get("properties") or {}).items():
            if name in ("classification", "source", "lastupdated", "unavailable"):
                continue
            path = f"{prefix}.{name}" if prefix else name
            desc = (sub.get("description") or sub.get("title") or "").strip().split("\n")[0]
            out.append((path, desc))
            out += _flatten_fields(sub, path, depth + 1)
    return out


def catalogue_rows(spec: dict, schema_name: str) -> list[dict]:
    """Rows for the data catalogue table (one per top-level attribute)."""
    props = spec["components"]["schemas"][schema_name].get("properties", {})
    rows = []
    for name, sub in props.items():
        desc = (sub.get("description") or "").strip().split("\n")[0]
        fields = _flatten_fields(sub)
        if not desc and fields:
            desc = f"{len(fields)} sub-fields"
        rows.append({"attribute": name, "description": desc,
                     "sub_fields": len(fields),
                     "fields": ", ".join(f for f, _ in fields[:40])})
    return rows


def openapi_chunks(spec: dict, schema_name: str, domain: str) -> list[Chunk]:
    chunks = []
    props = spec["components"]["schemas"][schema_name].get("properties", {})
    for name, sub in props.items():
        desc = (sub.get("description") or "").strip()
        fields = _flatten_fields(sub)
        lines = [f"[Myinfo API spec > {schema_name}.{name}]",
                 f"Attribute `{name}` of the Myinfo {schema_name} object. {desc}"]
        if fields:
            lines.append("Fields:")
            lines += [f"- `{p}`: {d}" if d else f"- `{p}`" for p, d in fields[:80]]
        text = "\n".join(lines)
        for i, piece in enumerate(_hard_split(text, CHUNK_TOKENS) if ntokens(text) > CHUNK_TOKENS else [text]):
            chunks.append(Chunk(piece, {"domain": domain, "source_type": "api_spec",
                                        "source_id": f"{schema_name}.{name}#{i}",
                                        "title": f"{schema_name}.{name}", "section": "Myinfo API spec",
                                        "product": "Myinfo API", "url": "", "error_codes": "",
                                        "synthetic": False}))
    meta = spec["components"]["schemas"].get("Meta", {})
    src = meta.get("properties", {}).get("source", {}).get("description", "")
    if src:
        chunks.append(Chunk(f"[Myinfo API spec > Meta]\nEvery Myinfo data item carries metadata "
                            f"`classification`, `source` and `lastupdated`.\nsource: {src}",
                            {"domain": domain, "source_type": "api_spec", "source_id": "Meta",
                             "title": "Meta", "section": "Myinfo API spec", "product": "Myinfo API",
                             "url": "", "error_codes": "", "synthetic": False}))
    return chunks
