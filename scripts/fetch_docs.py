"""Refresh the official documentation snapshots (public GitBook llms exports).

    python scripts/fetch_docs.py --domain singpass
    python scripts/fetch_docs.py --domain corppass

Follows the "Next part" pagination links and also downloads llms.txt (the page index
used to map each page to its source URL). Re-run ingest.py for the domain afterwards.
"""
from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from core.config import DOMAINS  # noqa: E402

SOURCES = {
    "singpass": ("https://docs.developer.singpass.gov.sg/docs/llms-full.txt",
                 "https://docs.developer.singpass.gov.sg/docs/llms.txt"),
    "corppass": ("https://docs.corppass.gov.sg/llms-full.txt", "https://docs.corppass.gov.sg/llms.txt"),
}


def get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "partner-support-copilot-poc"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", required=True, choices=list(DOMAINS))
    args = ap.parse_args()
    out: Path = DOMAINS[args.domain]["raw_dir"]
    out.mkdir(parents=True, exist_ok=True)
    full_url, index_url = SOURCES[args.domain]

    for old in out.glob("*.md"):
        old.unlink()
    url, part = full_url, 1
    while url and part <= 20:
        text = get(url)
        (out / f"part{part}.md").write_text(text)
        print(f"  part{part}.md  ({len(text):,} chars)  ← {url}")
        m = re.search(r"^> Next part: (\S+)", text, re.M)
        url, part = (m.group(1) if m else None), part + 1
    (out / "llms.txt").write_text(get(index_url))
    print(f"  llms.txt ← {index_url}\nDone. Now run: python scripts/ingest.py --domain {args.domain}")


if __name__ == "__main__":
    main()
