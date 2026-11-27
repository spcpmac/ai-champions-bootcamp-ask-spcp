"""Input/context guardrails: PII & secret redaction, injection filtering."""
from __future__ import annotations

import re
from dataclasses import dataclass, field

# Order matters: more specific / longer patterns first.
_PATTERNS: list[tuple[str, re.Pattern]] = [
    ("PRIVATE_KEY", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z ]*PRIVATE KEY-----")),
    ("JWT", re.compile(r"\beyJ[A-Za-z0-9_-]{5,}\.[A-Za-z0-9_-]{5,}(?:\.[A-Za-z0-9_-]*){1,3}")),
    ("JWK_PRIVATE", re.compile(r'"(d|p|q|dp|dq|qi)"\s*:\s*"[A-Za-z0-9_-]{16,}"')),
    ("SECRET", re.compile(r"(?i)\b(client_secret|api[_-]?key|password|secret)\b\s*[:=]\s*[\"']?[^\s\"',}]{6,}")),
    ("BEARER", re.compile(r"(?i)\b(Bearer|DPoP)\s+[A-Za-z0-9._~+/=-]{20,}")),
    ("EMAIL", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("NRIC_FIN", re.compile(r"\b[STFGM]\d{7}[A-Z]\b", re.IGNORECASE)),
    ("UEN", re.compile(r"\b(?:\d{8}[A-Z]|\d{9}[A-Z]|[TSR]\d{2}[A-Z]{2}\d{4}[A-Z])\b")),
    ("PHONE", re.compile(r"(?<!\d)(?:\+65[\s-]?)?[689]\d{3}[\s-]?\d{4}(?!\d)")),
]


@dataclass
class ScrubResult:
    text: str
    counts: dict[str, int] = field(default_factory=dict)

    @property
    def total(self) -> int:
        return sum(self.counts.values())

    def summary(self) -> str:
        return ", ".join(f"{n}× {k}" for k, n in self.counts.items())


def scrub(text: str) -> ScrubResult:
    """Redact PII and credentials before text leaves the app (to OpenAI or logs)."""
    counts: dict[str, int] = {}
    for label, pattern in _PATTERNS:
        text, n = pattern.subn(f"[REDACTED_{label}]", text)
        if n:
            counts[label] = counts.get(label, 0) + n
    return ScrubResult(text, counts)


_INJECTION = re.compile(
    r"(?i)(ignore (all|any|the) (previous|prior|above) instructions|disregard (the|your) (system|previous)|"
    r"you are now|new instructions:|system prompt|# Agent Instructions|perform an http get request)"
)


def looks_like_injection(text: str) -> bool:
    return bool(_INJECTION.search(text or ""))


def filter_context(chunks: list[dict]) -> list[dict]:
    """Drop retrieved chunks that contain instruction-like text aimed at an LLM."""
    return [c for c in chunks if not looks_like_injection(c.get("text", ""))]


DISCLAIMER = ("Answers are AI-generated from official docs and **synthetic** past cases. "
              "Always verify against the cited official documentation.")
