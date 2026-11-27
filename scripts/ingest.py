"""Build (or rebuild) one domain's knowledge base independently.

    python scripts/ingest.py --domain singpass            # chunk + embed + write Chroma
    python scripts/ingest.py --domain corppass --dry-run  # chunk only, write data/chunks/*.jsonl

Each domain lives in its own Chroma collection (kb_singpass / kb_corppass), so
re-ingesting one never touches the other.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import yaml  # noqa: E402

from core.chunking import (Chunk, chunk_page, openapi_chunks, parse_index,  # noqa: E402
                           slack_to_chunk, split_gitbook_pages, ticket_to_chunk)
from core.config import CHROMA_DIR, DATA_DIR, DOMAINS, OPENAPI_PATH, SYNTHETIC_DIR  # noqa: E402


_PRODUCT_RULES = {
    "singpass": [
        ("face-verification", "Singpass Face Verification"),
        ("sign-with-singpass", "Sign with Singpass"),
        ("legacy-myinfo-v3-v4", "Myinfo v3/v4 (legacy)"),
        ("myinfo", "Singpass Myinfo (v5)"),
        ("migration-guides", "Singpass Myinfo (v5)"),
        ("developer-portal", "Developer Portal"),
        ("pricing", "Developer Portal"),
        ("", "Singpass Login"),
    ],
    "corppass": [
        ("myinfo-business", "Myinfo Business"),
        ("developer-portal", "Corppass Developer Portal (CDP)"),
        ("authorization-info", "Authorization Info API"),
        ("", "Corppass Login"),
    ],
}


def _product_for(domain: str, url: str) -> str:
    u = url.lower()
    return next(p for key, p in _PRODUCT_RULES[domain] if key in u)


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text().splitlines() if l.strip()]


def build_chunks(domain: str) -> list[Chunk]:
    cfg = DOMAINS[domain]
    raw: Path = cfg["raw_dir"]
    index_path = raw / "llms.txt"
    index = parse_index(index_path.read_text()) if index_path.exists() else []

    chunks: list[Chunk] = []
    doc_files = sorted(p for p in raw.glob("*.md"))
    text = "\n".join(p.read_text() for p in doc_files)
    pages = split_gitbook_pages(text, index, default_url=cfg["doc_base_url"])
    for page in pages:
        base = {"domain": domain, "source_type": "doc", "source_id": page["url"] or page["title"],
                "product": _product_for(domain, page.get("url", "")), "synthetic": False}
        chunks.extend(chunk_page(page, base))
    print(f"  docs: {len(doc_files)} files → {len(pages)} pages → {len(chunks)} chunks")

    if OPENAPI_PATH.exists():
        spec = yaml.safe_load(OPENAPI_PATH.read_text())
        api = openapi_chunks(spec, cfg["openapi_schema"], domain)
        chunks.extend(api)
        print(f"  api_spec: {len(api)} chunks ({cfg['openapi_schema']} schema)")

    tickets = load_jsonl(SYNTHETIC_DIR / f"{domain}_tickets.jsonl")
    slack = load_jsonl(SYNTHETIC_DIR / f"{domain}_slack.jsonl")
    chunks += [ticket_to_chunk(t, domain) for t in tickets]
    chunks += [slack_to_chunk(s, domain) for s in slack]
    print(f"  tickets: {len(tickets)}  slack threads: {len(slack)}")

    # De-duplicate identical chunks (GitBook repeats some pages, e.g. brand guidelines)
    seen, unique = set(), []
    for c in chunks:
        if c.id not in seen:
            seen.add(c.id)
            unique.append(c)
    return unique


def write_chroma(domain: str, chunks: list[Chunk]) -> None:
    import chromadb

    from core.llm import embed

    from chromadb.config import Settings

    client = chromadb.PersistentClient(path=str(CHROMA_DIR), settings=Settings(anonymized_telemetry=False))
    name = DOMAINS[domain]["collection"]
    try:
        client.delete_collection(name)
    except Exception:
        pass
    col = client.create_collection(name, embedding_function=None, metadata={"hnsw:space": "cosine"})
    print(f"  embedding {len(chunks)} chunks …")
    vectors = embed([c.text for c in chunks])
    for i in range(0, len(chunks), 500):
        batch = chunks[i : i + 500]
        col.add(ids=[c.id for c in batch], documents=[c.text for c in batch],
                metadatas=[c.metadata for c in batch], embeddings=vectors[i : i + 500])
    print(f"  ✅ collection '{name}' now has {col.count()} chunks at {CHROMA_DIR}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", required=True, choices=list(DOMAINS))
    ap.add_argument("--dry-run", action="store_true", help="chunk only; skip embedding/Chroma")
    args = ap.parse_args()

    print(f"Ingesting domain '{args.domain}'")
    chunks = build_chunks(args.domain)
    out = DATA_DIR / "chunks" / f"{args.domain}.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(json.dumps({"id": c.id, "text": c.text, "metadata": c.metadata})
                             for c in chunks))
    by_type = Counter(c.metadata["source_type"] for c in chunks)
    print(f"  total unique chunks: {len(chunks)} {dict(by_type)} → {out}")
    if not args.dry_run:
        write_chroma(args.domain, chunks)


if __name__ == "__main__":
    main()
