"""Shared Streamlit UI helpers: styling, sidebar (domain, context), tables, sources, notices."""
from __future__ import annotations

import datetime as dt
import html
import re
from typing import Callable

import numpy as np
import pandas as pd
import streamlit as st

from core.config import APP_SHORT, DOMAINS, LANGUAGES
from core.guardrails import DISCLAIMER

PARTNER_TYPES = ["Not specified", "Government agency", "Bank / financial institution", "Insurance",
                 "Healthcare", "Education", "Telco", "Property / real estate", "Private enterprise / SME",
                 "System integrator / vendor"]
APP_TYPES = ["Not specified", "Web application", "Mobile app (iOS/Android)", "Backend / API only",
             "Kiosk / counter"]
EXPERIENCE = ["Not specified", "New to OIDC", "Familiar with OIDC/OAuth", "Experienced with FAPI 2.0"]

# Source types partners can search and see. Internal Slack threads are never shown in the app.
SOURCE_LABELS = {"doc": "📘 Official docs", "api_spec": "🧩 Myinfo API spec",
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
/* Read-only tables: cells wrap instead of truncating, and wide tables scroll rather than overflow. */
.ask-table {overflow-x: auto; margin: .25rem 0 1rem;}
.ask-table table {width: 100%; border-collapse: collapse; font-size: .88rem;}
.ask-table th, .ask-table td {text-align: left; vertical-align: top; padding: .4rem .6rem;
  border-bottom: 1px solid rgba(128,128,128,.25); white-space: normal; overflow-wrap: anywhere;}
.ask-table th {font-weight: 600; border-bottom-width: 2px;}
/* Flowcharts: cap the drawing size so it doesn't fill very large screens; shrink on narrow ones. */
[data-testid="stGraphVizChart"] svg {width: 100%; max-width: 900px; height: auto;}
/* Markdown tables (st.markdown) get the same wrapping and full width. */
[data-testid="stMarkdownContainer"] table {width: 100%;}
[data-testid="stMarkdownContainer"] th, [data-testid="stMarkdownContainer"] td {
  white-space: normal; overflow-wrap: anywhere; vertical-align: top;}
</style>
"""


def apply_style() -> None:
    st.markdown(_CSS, unsafe_allow_html=True)


def _cell(col: str, v, formats: dict[str, Callable[[object], str]]) -> str:
    if v is None or (not isinstance(v, str) and pd.isna(v)):
        return ""
    if col in formats:
        return formats[col](v)
    if isinstance(v, (bool, np.bool_)):
        return "✓" if v else ""
    if isinstance(v, (pd.Timestamp, dt.date)):
        return v.strftime("%Y-%m-%d")
    if isinstance(v, (float, np.floating)):
        return f"{v:.2f}".rstrip("0").rstrip(".")
    return str(v)


def table(df: pd.DataFrame, labels: dict[str, str] | None = None,
          formats: dict[str, Callable[[object], str]] | None = None) -> None:
    """Read-only table whose cells wrap. st.dataframe truncates long text, so use this instead.

    labels renames column headers; formats maps a column to a function that renders its values.
    """
    labels, formats = labels or {}, formats or {}
    head = "".join(f"<th>{html.escape(labels.get(c, str(c)))}</th>" for c in df.columns)
    rows = []
    for rec in df.itertuples(index=False):
        cells = "".join(
            f"<td>{html.escape(_cell(c, v, formats)).replace(chr(10), '<br>')}</td>"
            for c, v in zip(df.columns, rec))
        rows.append(f"<tr>{cells}</tr>")
    # One line with no blank lines, so Markdown passes it through as raw HTML.
    st.markdown(f'<div class="ask-table"><table><thead><tr>{head}</tr></thead>'
                f'<tbody>{"".join(rows)}</tbody></table></div>', unsafe_allow_html=True)


# ------------------------------------------------------------------ state helpers

def domain() -> str:
    return st.session_state.setdefault("domain", "singpass")


def cfg() -> dict:
    return DOMAINS[domain()]




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
    st.caption(f"{c['icon']} **{c['label']}** · {caption}")


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
    with st.expander(f"📚 Sources ({len(hits)})", expanded=expanded):
        for i, h in enumerate(hits, 1):
            m = h["metadata"]
            badge = SOURCE_LABELS.get(m["source_type"], m["source_type"])
            title = m.get("title", "")
            section = m.get("section", "")
            head = f"**[{i}] {title}**" + (f" › {section}" if section and section != title else "")
            if m.get("url"):
                head += f" · [open doc]({m['url']})"
            st.markdown(f"{head}  \n<small>{badge} · relevance {h.get('score', 0):.2f}</small>",
                        unsafe_allow_html=True)
            text = _public_text(h["text"])
            st.code(text[:1200] + ("…" if len(text) > 1200 else ""), language="markdown", wrap_lines=True)


def redaction_notice(result) -> None:
    if result.total:
        st.info(f"🛡️ Redacted {result.summary()} before sending to the AI model.")
