"""Central configuration: paths, model settings and per-domain definitions.

Everything domain-specific lives in DOMAINS so the same engine serves both
Singpass/Myinfo and Corppass/Myinfo Business.
"""
from __future__ import annotations

import os
from pathlib import Path

APP_NAME = "Ask Singpass: Better Partner Support Helper"
APP_SHORT = "Ask Singpass"

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
SYNTHETIC_DIR = DATA_DIR / "synthetic"
EVAL_DIR = DATA_DIR / "eval"
CHROMA_DIR = DATA_DIR / "chroma"
OPENAPI_PATH = ROOT / "ref" / "openapi.yaml"

# Retrieval / chunking parameters (also displayed on the Methodology page)
CHUNK_TOKENS = 800
CHUNK_OVERLAP_TOKENS = 100
RETRIEVE_K = 20          # candidates fetched from Chroma
FINAL_K = 6              # chunks kept after MMR
MMR_LAMBDA = 0.7         # relevance vs diversity trade-off

DEFAULT_CHAT_MODEL = "gpt-4.1-mini"
DEFAULT_EMBED_MODEL = "text-embedding-3-small"


def get_setting(name: str, default: str | None = None) -> str | None:
    """Read a setting from Streamlit secrets (if available) then env vars."""
    try:
        import streamlit as st

        if name in st.secrets:
            return str(st.secrets[name])
    except Exception:
        pass
    return os.environ.get(name, default)


def chat_model() -> str:
    return get_setting("OPENAI_CHAT_MODEL", DEFAULT_CHAT_MODEL)


def embed_model() -> str:
    return get_setting("OPENAI_EMBED_MODEL", DEFAULT_EMBED_MODEL)


COMMON_FLOW_STEPS = [
    "Not sure",
    "Onboarding / Developer Portal",
    "JWKS / key setup",
    "Pushed Authorization Request (PAR)",
    "Authorization redirect / callback",
    "Token request",
    "ID token decryption / validation",
    "Userinfo request",
    "Production go-live",
]

COMMON_ERROR_CODES = [
    "(none / not shown)",
    "invalid_request",
    "invalid_client",
    "invalid_grant",
    "invalid_scope",
    "invalid_dpop_proof",
    "use_dpop_nonce",
    "invalid_token",
    "invalid_request_uri",
    "unauthorized_client",
    "unsupported_grant_type",
    "access_denied",
    "login_required",
    "server_error",
    "temporarily_unavailable",
]

LANGUAGES = ["Not sure", "Java / Spring", "Node.js", "Python", ".NET / C#", "PHP", "Go",
             "Mobile (iOS/Android)", "Other"]

DOMAINS: dict[str, dict] = {
    "singpass": {
        "key": "singpass",
        "label": "Singpass / Myinfo",
        "short": "Singpass",
        "icon": "🔴",
        "color": "#C8102E",
        "collection": "kb_singpass",
        "raw_dir": RAW_DIR / "singpass",
        "doc_base_url": "https://docs.developer.singpass.gov.sg/docs",
        "products": ["Singpass Login", "Singpass Myinfo (v5)", "Myinfo v3/v4 (legacy)",
                     "Singpass Face Verification", "Sign with Singpass", "Developer Portal"],
        "flow_steps": COMMON_FLOW_STEPS,
        "error_codes": COMMON_ERROR_CODES,
        "openapi_schema": "Person",
        "scope_hint": "Singpass Login, Singpass Myinfo (person data), Face Verification, "
                      "Sign with Singpass, FAPI 2.0 / OIDC integration, the Singpass Developer Portal",
        "versions": ["New integration (FAPI 2.0 / Myinfo v5)", "Migrating from Myinfo v3",
                     "Migrating from Myinfo v4", "Migrating Login app to FAPI 2.0"],
        "sample_questions": [
            "What changed for Singpass Login under FAPI 2.0?",
            "How do I generate a DPoP proof for the token request?",
            "Why would the token endpoint return invalid_client?",
            "How do I migrate a Myinfo v3 app to Myinfo v5?",
        ],
    },
    "corppass": {
        "key": "corppass",
        "label": "Corppass / Myinfo Business",
        "short": "Corppass",
        "icon": "🔵",
        "color": "#1F4E9E",
        "collection": "kb_corppass",
        "raw_dir": RAW_DIR / "corppass",
        "doc_base_url": "https://docs.corppass.gov.sg",
        "products": ["Corppass Login", "Myinfo Business", "Corppass Developer Portal (CDP)",
                     "Authorization Info API"],
        "flow_steps": COMMON_FLOW_STEPS,
        "error_codes": COMMON_ERROR_CODES,
        "openapi_schema": "Entity",
        "scope_hint": "Corppass Login, Myinfo Business (entity data), the Corppass Authorization API "
                      "(FAPI 2.0), auth_info / entity_info / person_info claims, the Corppass Developer Portal",
        "versions": ["New integration (FAPI 2.0)", "Migrating from legacy Corppass OIDC",
                     "Migrating from Myinfo Business v1/v2"],
        "sample_questions": [
            "What is authentication_context_type and when is it required?",
            "What does invalid_dpop_proof mean on the PAR endpoint?",
            "How do I whitelist Corppass IP addresses for outgoing traffic?",
            "What claims are in entity_info?",
        ],
    },
}

SOURCE_TYPES = {
    "doc": "📘 Official docs",
    "ticket": "🎫 Support tickets (synthetic)",
    "slack": "💬 Slack threads (synthetic)",
    "api_spec": "🧩 Myinfo API spec",
}
