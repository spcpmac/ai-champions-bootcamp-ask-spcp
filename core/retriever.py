"""Retrieval over the per-domain Chroma collections (read-only at runtime)."""
from __future__ import annotations

import json
import re
from collections import Counter

import numpy as np

from core.chunking import ERROR_CODE_RE
from core.config import CHROMA_DIR, DATA_DIR, DOMAINS, FINAL_K, MMR_LAMBDA, RETRIEVE_K
from core.guardrails import filter_context
from core.llm import embed

try:
    import streamlit as st
    _cache = st.cache_resource
except Exception:  # pragma: no cover - scripts without streamlit runtime
    def _cache(fn=None, **_):
        return fn


@_cache(show_spinner=False)
def _client():
    import chromadb

    from chromadb.config import Settings

    return chromadb.PersistentClient(path=str(CHROMA_DIR), settings=Settings(anonymized_telemetry=False))


def get_collection(domain: str):
    return _client().get_collection(DOMAINS[domain]["collection"], embedding_function=None)


def kb_ready(domain: str) -> bool:
    try:
        return get_collection(domain).count() > 0
    except Exception:
        return False


def kb_stats(domain: str) -> dict:
    """Chunk counts per source type (from Chroma if built, else the chunk dump)."""
    try:
        metas = get_collection(domain).get(include=["metadatas"])["metadatas"]
    except Exception:
        path = DATA_DIR / "chunks" / f"{domain}.jsonl"
        metas = [json.loads(l)["metadata"] for l in path.read_text().splitlines()] if path.exists() else []
    return {"total": len(metas),
            "by_source": dict(Counter(m["source_type"] for m in metas)),
            "by_product": dict(Counter(m.get("product", "") for m in metas)),
            "doc_pages": len({m.get("url") or m.get("title") for m in metas if m["source_type"] == "doc"})}


ERROR_CODE_BONUS = 0.05  # added to relevance of chunks tagged with the queried error code
LEGACY_PENALTY = 0.08   # subtracted from relevance of legacy-spec chunks for non-legacy questions
_LEGACY_QUERY = re.compile(r"(?i)\b(legacy|v[1-4]\b|myinfo\s*v?[34]\b|pre-?fapi|old(er)? (api|spec|version))")


def is_legacy(meta: dict) -> bool:
    """Legacy (superseded) specs, e.g. Myinfo v3/v4 and pre-FAPI 2.0 docs, identified by URL."""
    return "/legacy-" in (meta.get("url") or "")


def _mmr(query: np.ndarray, docs: np.ndarray, k: int, lam: float, penalty: np.ndarray | None = None) -> list[int]:
    qn = query / (np.linalg.norm(query) + 1e-9)
    dn = docs / (np.linalg.norm(docs, axis=1, keepdims=True) + 1e-9)
    rel = dn @ qn - (penalty if penalty is not None else 0)
    sim = dn @ dn.T
    chosen: list[int] = []
    cand = list(range(len(docs)))
    while cand and len(chosen) < k:
        if not chosen:
            best = max(cand, key=lambda i: rel[i])
        else:
            best = max(cand, key=lambda i: lam * rel[i] - (1 - lam) * max(sim[i][j] for j in chosen))
        chosen.append(best)
        cand.remove(best)
    return chosen


def retrieve(domain: str, query: str, source_types: list[str] | None = None,
             k: int = FINAL_K, fetch_k: int = RETRIEVE_K, error_code: str | None = None) -> list[dict]:
    """Semantic search + MMR re-ranking. Returns [{text, metadata, score}]."""
    col = get_collection(domain)
    where = {"source_type": {"$in": source_types}} if source_types else None
    qvec = np.array(embed([query])[0])
    res = col.query(query_embeddings=[qvec.tolist()], n_results=fetch_k, where=where,
                    include=["documents", "metadatas", "embeddings", "distances"])
    docs, metas = res["documents"][0], res["metadatas"][0]
    if not docs:
        return []
    embs = np.array(res["embeddings"][0])
    dists = res["distances"][0]
    # Re-weight relevance before MMR selection:
    #  - demote legacy specs unless the question is explicitly about legacy versions
    #  - boost chunks tagged with the error code (selected in a form, or typed in the question)
    if not error_code:
        m = ERROR_CODE_RE.search(query)
        error_code = m.group(0) if m else None
    legacy_q = bool(_LEGACY_QUERY.search(query))
    penalty = np.array([
        (LEGACY_PENALTY if is_legacy(m) and not legacy_q else 0.0)
        - (ERROR_CODE_BONUS if error_code and error_code in (m.get("error_codes") or "").split(",") else 0.0)
        for m in metas])
    order = _mmr(qvec, embs, k, MMR_LAMBDA, penalty)
    hits = [{"text": docs[i], "metadata": metas[i], "score": round(1 - dists[i], 3)} for i in order]
    return filter_context(hits)


def format_context(hits: list[dict]) -> str:
    """Numbered <source> blocks for the prompt. Internal ticket IDs are hidden from the model and the UI."""
    blocks = []
    for i, h in enumerate(hits, 1):
        m = h["metadata"]
        text = re.sub(r"\[Support ticket [A-Z]+-\d+ — ", "[Past resolved case — ", h["text"])
        label = {"doc": "Official doc (LEGACY spec)" if is_legacy(m) else "Official doc", "ticket": "Historical ticket (synthetic)",
                 "slack": "Slack thread (synthetic)", "api_spec": "Myinfo API spec"}[m["source_type"]]
        blocks.append(f'<source id="{i}" type="{label}" title="{m.get("title", "")}">\n{text}\n</source>')
    return "\n\n".join(blocks)
