"""Shared Streamlit UI helpers: styling, sidebar (domain, audience, context), sources, notices."""
from __future__ import annotations

import re
from typing import Callable

import streamlit as st

from core.config import APP_SHORT, DOMAINS, LANGUAGES, SOURCE_TYPES
from core.guardrails import DISCLAIMER

PARTNER_TYPES = ["Not specified", "Government agency", "Bank / financial institution", "Insurance",
                 "Healthcare", "Education", "Telco", "Property / real estate", "Private enterprise / SME",
                 "System integrator / vendor"]
APP_TYPES = ["Not specified", "Web application", "Mobile app (iOS/Android)", "Backend / API only",
             "Kiosk / counter"]
EXPERIENCE = ["Not specified", "New to OIDC", "Familiar with OIDC/OAuth", "Experienced with FAPI 2.0"]

# Partners see official docs, the API spec and sanitised past cases. Internal Slack threads are
# officer-only.
PARTNER_SOURCES = {"doc": "📘 Official docs", "api_spec": "🧩 Myinfo API spec",
                   "ticket": "🎫 Past resolved cases"}

_CSS = """
<style>
/* Streamlit's fixed top bar is 3.75rem tall; keep content just below it. */
.block-container {padding-top: 4.25rem; padding-bottom: 1rem;}
h1 {font-size: 1.75rem !important; line-height: 1.3 !important; padding: .1rem 0 .1rem 0 !important;}
h2 {font-size: 1.35rem !important;}
h3 {font-size: 1.15rem !important;}
[data-testid="stChatMessage"] {padding: .5rem .75rem;}
[data-testid="stExpander"] details summary p {font-size: .9rem;}
[data-testid="stSidebarUserContent"] {padding-top: 1rem;}
</style>
"""


def apply_style() -> None:
    st.markdown(_CSS, unsafe_allow_html=True)


# ------------------------------------------------------------------ state helpers

def domain() -> str:
    return st.session_state.setdefault("domain", "singpass")


def cfg() -> dict:
    return DOMAINS[domain()]


def is_officer() -> bool:
    return bool(st.session_state.get("officer_mode", False))


def audience() -> str:
    return "officer" if is_officer() else "partner"


def source_options() -> dict[str, str]:
    return SOURCE_TYPES if is_officer() else PARTNER_SOURCES


# ------------------------------------------------------------------ layout pieces

def sidebar() -> None:
    with st.sidebar:
        st.markdown(f"### 🛡️ {APP_SHORT}")
        st.radio("Integration", list(DOMAINS), key="domain",
                 format_func=lambda k: f"{DOMAINS[k]['icon']} {DOMAINS[k]['label']}")
        with st.expander("🧭 About your integration (optional)", expanded=False):
            st.caption("Generic, non-identifying details that tailor every answer. Don't enter names, "
                       "NRIC, UEN, client IDs or credentials.")
            st.selectbox("Organisation type", PARTNER_TYPES, key="ctx_partner")
            st.selectbox("App type", APP_TYPES, key="ctx_app")
            st.selectbox("Tech stack", LANGUAGES, key="ctx_lang")
            st.selectbox("Environment", ["Not specified", "Staging", "Production"], key="ctx_env")
            st.selectbox("Team experience", EXPERIENCE, key="ctx_exp")
        st.toggle("🧑‍💼 Support officer mode", key="officer_mode",
                  help="For Singpass/Corppass support staff: shows internal Slack threads and ticket IDs, "
                       "and drafts replies to partners instead of support requests.")
        st.caption("⚠️ " + DISCLAIMER)


def profile_text() -> str:
    parts = {"Organisation type": st.session_state.get("ctx_partner"),
             "App type": st.session_state.get("ctx_app"), "Tech stack": st.session_state.get("ctx_lang"),
             "Environment": st.session_state.get("ctx_env"), "Experience": st.session_state.get("ctx_exp")}
    return "; ".join(f"{k}: {v}" for k, v in parts.items() if v and v not in ("Not specified", "Not sure"))


IMPORTANT_NOTICE = """\
**IMPORTANT NOTICE:** This web application is a prototype developed for **educational purposes only**. \
The information provided here is **NOT intended for real-world usage** and should not be relied upon for \
making any decisions, especially those related to financial, legal, or healthcare matters.

Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume \
full responsibility for how you use any generated output.

Always consult with qualified professionals for accurate and personalised advice.
"""


def important_notice() -> None:
    # Collapsed to save space, but the label itself carries the key message.
    with st.expander("⚠️ **IMPORTANT NOTICE:** educational prototype only, not for real-world use. "
                     "Tap to read.", expanded=False):
        st.markdown(IMPORTANT_NOTICE)


def page_header(title: str, caption: str) -> None:
    c = cfg()
    st.title(title)
    mode = "Support officer mode" if is_officer() else "Partner self-service"
    st.caption(f"{c['icon']} **{c['label']}** · {mode} · {caption}")


def suggestion_chips(options: list[str], key: str, on_pick: Callable[[str], None], label: str) -> None:
    """Compact clickable chips (st.pills); picking one calls on_pick(text) and clears the selection."""
    if not options:
        return

    def _cb():
        val = st.session_state.get(key)
        if val:
            on_pick(val)
            st.session_state[key] = None

    st.pills(label, options, selection_mode="single", key=key, on_change=_cb)


def require_kb() -> bool:
    """Show a helpful message if the knowledge base or API key is missing."""
    from core.config import get_setting
    from core.retriever import kb_ready

    if not get_setting("OPENAI_API_KEY"):
        st.error("`OPENAI_API_KEY` is not configured. Add it to `.streamlit/secrets.toml`.")
        return False
    if not kb_ready(domain()):
        st.warning(f"The **{cfg()['label']}** knowledge base has not been built yet. Run:\n\n"
                   f"```bash\npython scripts/ingest.py --domain {domain()}\n```")
        return False
    return True


def _public_text(text: str) -> str:
    """Hide internal ticket identifiers from partner-facing views."""
    return re.sub(r"\[Support ticket [A-Z]+-\d+ — ", "[Past resolved case — ", text)


def render_sources(hits: list[dict], expanded: bool = False) -> None:
    if not hits:
        return
    officer = is_officer()
    labels = source_options() | {"ticket": SOURCE_TYPES["ticket"] if officer else "🎫 Past resolved case"}
    with st.expander(f"📚 Sources ({len(hits)})", expanded=expanded):
        for i, h in enumerate(hits, 1):
            m = h["metadata"]
            badge = labels.get(m["source_type"], m["source_type"])
            title = m.get("title", "")
            section = m.get("section", "")
            head = f"**[{i}] {title}**" + (f" › {section}" if section and section != title else "")
            if m.get("url"):
                head += f" · [open doc]({m['url']})"
            if officer and m["source_type"] in ("ticket", "slack"):
                head += f" · `{m.get('source_id', '')}`"
            st.markdown(f"{head}  \n<small>{badge} · relevance {h.get('score', 0):.2f}</small>",
                        unsafe_allow_html=True)
            text = h["text"] if officer else _public_text(h["text"])
            st.code(text[:1200] + ("…" if len(text) > 1200 else ""), language="markdown", wrap_lines=True)


def redaction_notice(result) -> None:
    if result.total:
        st.info(f"🛡️ Redacted {result.summary()} before sending to the AI model.")
