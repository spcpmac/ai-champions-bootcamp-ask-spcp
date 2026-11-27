"""Evaluate retrieval (hit@k, MRR) and optionally answer faithfulness for one domain.

    python scripts/eval.py --domain singpass
    python scripts/eval.py --domain corppass --judge     # also LLM-judge faithfulness

Results are merged into data/eval/results.json (shown on the Methodology page).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pydantic import BaseModel  # noqa: E402

from core import llm  # noqa: E402
from core.config import DOMAINS, EVAL_DIR, FINAL_K, chat_model  # noqa: E402
from core.prompts import assistant_system  # noqa: E402
from core.retriever import format_context, retrieve  # noqa: E402


class Verdict(BaseModel):
    faithful: bool
    reason: str


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", required=True, choices=list(DOMAINS))
    ap.add_argument("--judge", action="store_true")
    args = ap.parse_args()
    cfg = DOMAINS[args.domain]
    golden = json.loads((EVAL_DIR / f"{args.domain}.json").read_text())

    hits_at_k, rr, faithful = 0, 0.0, []
    for g in golden:
        hits = retrieve(args.domain, g["q"], source_types=["doc", "api_spec"])
        urls = [h["metadata"].get("url", "") for h in hits]
        rank = next((i + 1 for i, u in enumerate(urls) if g["expect"] in u), None)
        hits_at_k += bool(rank)
        rr += 1 / rank if rank else 0
        line = f"{'✅' if rank else '❌'} rank={rank or '-'}  {g['q']}"
        if args.judge:
            ans = llm.chat([{"role": "system", "content": assistant_system(cfg["label"], cfg["scope_hint"], "")},
                            {"role": "user", "content": f"<sources>\n{format_context(hits)}\n</sources>\n\n"
                                                        f"Question: {g['q']}"}])
            v = llm.chat_structured([
                {"role": "system", "content": "You judge whether an answer is fully supported by the sources. "
                                              "Unsupported specifics (values, parameters, limits) = not faithful."},
                {"role": "user", "content": f"Sources:\n{format_context(hits)}\n\nAnswer:\n{ans}"}], Verdict)
            faithful.append(v.faithful)
            line += f"  faithful={v.faithful}"
            if not v.faithful:
                line += f"\n      judge: {v.reason}"
        print(line)

    n = len(golden)
    row = {"domain": cfg["label"], "questions": n, f"hit@{FINAL_K}": f"{hits_at_k / n:.0%}",
           "MRR": round(rr / n, 2), "faithfulness": f"{sum(faithful) / n:.0%}" if faithful else "not run",
           "model": chat_model()}
    print(row)
    out = EVAL_DIR / "results.json"
    results = json.loads(out.read_text()) if out.exists() else []
    results = [r for r in results if r["domain"] != cfg["label"]] + [row]
    out.write_text(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
