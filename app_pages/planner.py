"""UC3 — Integration Planner: personalised onboarding / migration checklist."""
from __future__ import annotations

import streamlit as st

from core import llm
from core.catalogue import data_catalogue
from core.guardrails import scrub
from core.prompts import BASE_RULES, IntegrationPlan, planner_system
from core.retriever import format_context, retrieve
from core.ui import (APP_TYPES, audience, cfg, domain, is_officer, page_header, profile_text, redaction_notice,
                     render_sources, require_kb)

page_header("🗺️ Integration Planner", "A step-by-step onboarding or migration plan tailored to your scenario")
if not require_kb():
    st.stop()
c = cfg()
catalogue = data_catalogue(domain())
officer = is_officer()
key = f"plan_{domain()}_{audience()}"

with st.form("planner"):
    a, b, d = st.columns(3)
    product = a.selectbox("Product", c["products"])
    version = b.selectbox("Scenario", c["versions"])
    app_type = d.selectbox("App type", APP_TYPES[1:])
    a, b = st.columns(2)
    stage = a.select_slider("Current stage", ["Not started", "Staging app created", "Building",
                                              "Testing in staging", "Ready for production"])
    data_needed = b.multiselect(f"Myinfo data needed ({c['openapi_schema']} attributes)",
                                catalogue["attribute"].tolist(),
                                help="Leave empty if you only need login / authentication.")
    notes = st.text_input("Anything else? (generic, non-identifying)",
                          placeholder="e.g. we already have an OIDC library, must go live by Q2")
    go = st.form_submit_button("🧭 Build my plan", type="primary")

if go:
    clean = scrub(notes)
    redaction_notice(clean)
    profile = (f"Product: {product}; Scenario: {version}; App type: {app_type}; Stage: {stage}; "
               f"Data needed: {', '.join(data_needed) or 'none (login only)'}; Notes: {clean.text or 'none'}; "
               f"{profile_text()}")
    query = f"{product} {version} {app_type} onboarding steps requirements checklist go-live"
    with st.spinner("Gathering requirements…"):
        hits = retrieve(domain(), query, source_types=["doc"], k=6)
        hits += retrieve(domain(), f"{version} {product} {' '.join(data_needed[:5])}",
                         source_types=["doc", "api_spec"], k=3)
        hits += retrieve(domain(), f"{product} {version} common problems", source_types=["ticket", "slack"] if officer else ["ticket"], k=3)
    seen, uniq = set(), []
    for h in hits:
        if h["text"] not in seen:
            seen.add(h["text"])
            uniq.append(h)
    with st.spinner("Writing a tailored plan…"):
        try:
            plan = llm.chat_structured([
                {"role": "system", "content": planner_system(c["label"])},
                {"role": "user", "content": f"<sources>\n{format_context(uniq, public=not officer)}\n</sources>\n\nPartner profile: {profile}"},
            ], IntegrationPlan)
        except Exception as e:  # noqa: BLE001
            st.error(f"Planning failed: {e}")
            st.stop()
    st.session_state[key] = {"plan": plan, "hits": uniq, "profile": profile, "data": data_needed, "qa": []}

state = st.session_state.get(key)
if state:
    plan: IntegrationPlan = state["plan"]
    st.subheader("Your plan")
    st.markdown(plan.overview)

    total = len(plan.checklist)
    done = sum(st.session_state.get(f"{key}_item_{i}", False) for i in range(total))
    st.progress(done / max(total, 1), text=f"Progress: {done}/{total} tasks")
    tabs = st.tabs(["Prepare", "Build", "Test", "Go-live"])
    for tab, phase in zip(tabs, ["Prepare", "Build", "Test", "Go-live"]):
        with tab:
            items = [(i, it) for i, it in enumerate(plan.checklist) if it.phase == phase]
            if not items:
                st.caption("Nothing specific for this phase.")
            for i, it in items:
                st.checkbox(f"**{it.task}**", key=f"{key}_item_{i}")
                st.caption(it.detail)

    if plan.pitfalls:
        st.markdown("#### ⚠️ Pitfalls seen in past cases")
        for p in plan.pitfalls:
            st.markdown(f"- {p}")

    if state["data"]:
        st.markdown("#### Data you asked for")
        sel = catalogue[catalogue["attribute"].isin(state["data"])]
        st.dataframe(sel, hide_index=True, width="stretch")
        st.caption("Request only what the stated purpose needs (data minimisation, per Myinfo key principles).")

    render_sources(state["hits"])

    st.markdown("#### Ask about this plan")
    for q, a in state["qa"]:
        st.chat_message("user").markdown(q)
        st.chat_message("assistant").markdown(a)
    q = st.chat_input("e.g. What exactly do I need for the JWKS step?")
    if q:
        qc = scrub(q)
        hits = retrieve(domain(), qc.text, k=5,
                        source_types=None if officer else ["doc", "api_spec", "ticket"])
        plan_md = "\n".join(f"- [{it.phase}] {it.task}: {it.detail}" for it in plan.checklist)
        ans = llm.chat([
            {"role": "system", "content": f"You answer follow-up questions about a {c['label']} integration plan.\n"
                                          f"{BASE_RULES}"},
            {"role": "user", "content": f"Partner profile: {state['profile']}\n\nPlan:\n{plan_md}\n\n"
                                        f"<sources>\n{format_context(hits, public=not officer)}\n</sources>\n\nQuestion: {qc.text}"},
        ])
        state["qa"].append((qc.text, ans))
        st.rerun()
