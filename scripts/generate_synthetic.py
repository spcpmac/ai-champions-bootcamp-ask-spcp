"""Use the LLM to create more SYNTHETIC tickets grounded in real doc sections.

    python scripts/generate_synthetic.py --domain corppass --n 20

New tickets are appended to data/synthetic/{domain}_tickets.jsonl (marked synthetic).
Review them by hand before committing, then re-run scripts/ingest.py for that domain.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import Literal, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pydantic import BaseModel  # noqa: E402

from core.config import DATA_DIR, DOMAINS, SYNTHETIC_DIR  # noqa: E402
from core.llm import chat_structured  # noqa: E402

Category = Literal["Authentication flow", "Keys & JWKS", "Configuration / Portal", "Myinfo data",
                   "Migration", "Network & TLS", "Onboarding & Compliance", "Availability / Incident"]


class Ticket(BaseModel):
    product: str
    category: Category
    environment: Literal["Staging", "Production"]
    flow_step: str
    error_code: Optional[str]
    subject: str
    description: str
    resolution: str
    tags: list[str]
    escalated_to_engineer: bool


class TicketBatch(BaseModel):
    tickets: list[Ticket]


SYSTEM = """You create realistic but entirely FICTIONAL partner-support tickets for a government
identity platform's support team. Base every ticket strictly on the documentation excerpt provided:
the root cause and resolution must be correct according to it. Never include real names, NRIC/FIN,
UENs, emails, phone numbers, tokens or keys. Refer to partners generically (e.g. "a bank", "an agency")."""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", required=True, choices=list(DOMAINS))
    ap.add_argument("--n", type=int, default=20)
    args = ap.parse_args()
    cfg = DOMAINS[args.domain]

    chunks = [json.loads(l) for l in (DATA_DIR / "chunks" / f"{args.domain}.jsonl").read_text().splitlines()]
    candidates = [c for c in chunks if c["metadata"]["source_type"] == "doc"
                  and (c["metadata"]["error_codes"] or "FAQ" in c["metadata"]["title"]
                       or "Migration" in c["metadata"]["title"] or "JWKS" in c["text"][:200])]
    rng = random.Random()
    out_path = SYNTHETIC_DIR / f"{args.domain}_tickets.jsonl"
    existing = [json.loads(l) for l in out_path.read_text().splitlines() if l.strip()] if out_path.exists() else []
    prefix = "SP" if args.domain == "singpass" else "CP"
    next_id = 2000 + len(existing)

    made = 0
    while made < args.n:
        doc = rng.choice(candidates)
        batch = chat_structured([
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": f"Products: {cfg['products']}\nFlow steps: {cfg['flow_steps']}\n\n"
                                        f"Documentation excerpt:\n<doc>\n{doc['text']}\n</doc>\n\n"
                                        "Write 2 distinct tickets."},
        ], TicketBatch)
        with out_path.open("a") as f:
            for t in batch.tickets:
                next_id += 1
                rec = t.model_dump() | {
                    "id": f"{prefix}-{next_id}",
                    "resolution_time_hrs": round(rng.uniform(1, 72), 1),
                    "created_at": (date(2025, 6, 1) + timedelta(days=rng.randrange(530))).isoformat(),
                    "synthetic": True, "grounded_in": doc["metadata"]["url"],
                }
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                made += 1
        print(f"  {made}/{args.n} (grounded in: {doc['metadata']['title']})")
    print(f"Appended {made} tickets to {out_path}. Review, then run ingest.py --domain {args.domain}.")


if __name__ == "__main__":
    main()
