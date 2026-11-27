"""UC2 — Integration Troubleshooter: structured form → ranked diagnosis + similar past cases."""
from __future__ import annotations

import pandas as pd
import streamlit as st

from core import llm
from core.config import LANGUAGES
from core.guardrails import scrub
from core.prompts import Diagnosis, support_request_system, troubleshooter_system
from core.retriever import format_context, retrieve
from core.ui import (audience, cfg, domain, is_officer, page_header, profile_text, redaction_notice,
                     render_sources, require_kb)

page_header("🩺 Integration Troubleshooter", "Describe what's failing and get a ranked diagnosis")
if not require_kb():
    st.stop()
c = cfg()
officer = is_officer()
key = f"diag_{domain()}_{audience()}"

with st.form("troubleshoot", border=True):
    a, b, d = st.columns(3)
    product = a.selectbox("Product", c["products"])
    step = b.selectbox("Where does it fail?", c["flow_steps"])
    error = d.selectbox("Error code", c["error_codes"])
    a, b, d = st.columns(3)
    http = a.selectbox("HTTP status", ["Unknown", "400", "401", "403", "404", "500", "502", "503", "Timeout"])
    env = b.selectbox("Environment", ["Staging", "Production", "Both"])
    lang = d.selectbox("Partner tech stack" if officer else "Your tech stack", LANGUAGES)
    since = st.radio("Started", ["New integration", "After a change (keys, config, deploy)",
                                 "Suddenly, no known change", "Intermittent"], horizontal=True)
    details = st.text_area(("What is the partner seeing?" if officer else "What are you seeing?")
                           + " Paste the error_description or logs; secrets and PII are redacted automatically.",
                           height=90,
                           placeholder="e.g. PAR call returns 401 invalid_dpop_proof since we moved servers…")
    submitted = st.form_submit_button("🔍 Diagnose", type="primary")

if submitted:
    clean = scrub(details)
    redaction_notice(clean)
    err = None if error.startswith("(") else error
    issue = (f"Product: {product}\nFailing step: {step}\nError code: {err or 'none'}\nHTTP status: {http}\n"
             f"Environment: {env}\nTech stack: {lang}\nStarted: {since}\nDetails: {clean.text or 'n/a'}")
    query = f"{product} {step} {err or ''} {http} {clean.text[:300]}"
    with st.spinner("Searching docs and past cases…"):
        doc_hits = retrieve(domain(), query, source_types=["doc", "api_spec"], k=5, error_code=err)
        case_hits = retrieve(domain(), query, source_types=["ticket", "slack"] if officer else ["ticket"],
                             k=4, error_code=err)
    hits = doc_hits + case_hits
    with st.spinner("Diagnosing…"):
        try:
            diag = llm.chat_structured([
                {"role": "system", "content": troubleshooter_system(c["label"], audience())},
                {"role": "user", "content": f"<sources>\n{format_context(hits, public=not officer)}\n</sources>\n\n"
                                            f"User context: {profile_text() or 'n/a'}\n\nIssue:\n{issue}"},
            ], Diagnosis)
        except Exception as e:  # noqa: BLE001
            st.error(f"Diagnosis failed: {e}")
            st.stop()
    st.session_state[key] = {"diag": diag, "hits": hits, "cases": case_hits, "issue": issue}

state = st.session_state.get(key)
if state:
    diag: Diagnosis = state["diag"]
    st.subheader("Diagnosis")
    st.markdown(diag.summary)
    if diag.needs_support:
        st.warning(("⬆️ **Escalate to engineering:** " if officer else "📨 **Contact partner support:** ")
                   + diag.support_reason)
    else:
        st.success("✅ Likely resolvable by support, no escalation needed." if officer
                   else "✅ This looks fixable on your side. Work through the checklist below.")

    left, right = st.columns([3, 2], gap="medium")
    with left:
        st.markdown("##### Likely causes")
        icon = {"High": "🔴", "Medium": "🟠", "Low": "🟢"}
        for cause in diag.likely_causes:
            with st.container(border=True):
                st.markdown(f"{icon[cause.likelihood]} **{cause.cause}** · _{cause.likelihood}_")
                st.caption(cause.evidence)
        st.markdown("##### Fix checklist")
        done = 0
        for i, s in enumerate(diag.fix_steps):
            done += st.checkbox(s, key=f"{key}_fix_{i}")
        st.progress(done / max(len(diag.fix_steps), 1), text=f"{done}/{len(diag.fix_steps)} steps checked")
    with right:
        st.markdown("##### " + ("Ask the partner for" if officer else "Details worth checking"))
        for q in diag.info_to_gather:
            st.markdown(f"- {q}")
        st.markdown("##### " + ("Similar historical cases" if officer else "How others resolved similar issues"))
        rows = []
        for h in state["cases"]:
            m, text = h["metadata"], h["text"]
            outcome = (text.split("Resolution:\n", 1)[-1] if "Resolution:\n" in text
                       else text.split("Outcome:", 1)[-1]).strip()
            row = {"Case": m.get("title"), "Resolution": outcome[:220], "Match": h["score"]}
            if officer:
                row = {"ID": m.get("source_id"), "Type": m["source_type"]} | row
            rows.append(row)
        if rows:
            st.dataframe(pd.DataFrame(rows), hide_index=True, width="stretch",
                         column_config={"Match": st.column_config.ProgressColumn(min_value=0, max_value=1,
                                                                                 width="small"),
                                        "Resolution": st.column_config.TextColumn(width="large")})
        else:
            st.caption("No similar cases found.")

    if not officer:
        if st.button("📨 Still stuck? Draft a support request", type="secondary"):
            fixes = "\n".join(f"- {s}" for s in diag.fix_steps)
            with st.spinner("Drafting…"):
                state["request"] = llm.chat([
                    {"role": "system", "content": support_request_system(c["label"])},
                    {"role": "user", "content": f"Issue details:\n{state['issue']}\n\nDiagnosis: {diag.summary}\n"
                                                f"Suggested checks already given:\n{fixes}"}])
        if state.get("request"):
            with st.expander("📨 Support request draft: remove anything sensitive before sending", expanded=True):
                st.code(state["request"], language="markdown", wrap_lines=True)
    render_sources(state["hits"])
