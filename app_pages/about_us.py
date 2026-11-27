"""About Us — project scope, objectives, data sources and features."""
from __future__ import annotations

import pandas as pd
import streamlit as st

from core.config import APP_NAME, DOMAINS
from core.retriever import kb_stats
from core.ui import table

st.title("ℹ️ About Us")
st.caption(f"{APP_NAME}: proof of concept")

st.markdown("""
### The problem
Organisations integrating with Singpass and Corppass, and the support teams that help them, rely on a large
and growing body of knowledge: authentication flows, API specifications, integration errors, configuration
issues and production incidents. Today that knowledge is spread across Slack discussions, support tickets,
technical documentation and individual engineers' memories. Partners wait for answers, support officers
repeat the same investigations, and too many questions end up escalated to engineers.

### Our solution
**Ask Singpass** is a conversational assistant built on a large language model (LLM) with
retrieval-augmented generation (RAG). It brings official developer documentation and past resolved cases
into one knowledge base, so **integrating partners can help themselves first**. They get grounded, cited
answers, a guided troubleshooter and a tailored integration plan at any time. When self-service isn't
enough, the assistant drafts a well-structured support request, so the first message to support already
contains what's needed.

### Objectives
- **Self-service first:** partners resolve common integration issues without raising a ticket.
- **Faster, consistent responses:** every answer cites the official documentation it is based on.
- **Fewer escalations:** past resolutions are available to every partner.
- **Better tickets:** when partners do need help, their requests arrive complete and free of secrets.

### Scope
- Two integration domains, each with its own knowledge base, chosen with the sidebar switcher:
  **Singpass / Myinfo** and **Corppass / Myinfo Business**.
- Users: developers at integrating organisations.
- POC only. Past cases are **synthetic**, and no production data is used.
""")

st.markdown("### How the app meets the requirements")
table(pd.DataFrame([
    ("Consolidate information",
     "One knowledge base per domain combining the official Singpass / Corppass developer docs, the Myinfo "
     "OpenAPI spec and past resolved cases, with every answer citing its source"),
    ("Personalise user experience",
     "Sidebar 'About your integration' (organisation type, app type, tech stack, environment, experience), "
     "the Troubleshooter form and the Planner form. All of these are generic and non-identifying, and PII "
     "and secrets are redacted automatically"),
    ("Enhance understanding",
     "Explanations pitched at your experience level, suggested follow-up questions, Q&A on your plan, "
     "and ranked causes with the evidence for each"),
    ("Present information effectively",
     "Chat text with citations, interactive forms, checklists with progress bars, data tables "
     "(similar cases, data catalogue) and charts (Knowledge Insights)"),
], columns=["Requirement", "How Ask Singpass delivers it"]))

st.markdown("### Data sources")
rows = []
for key, d in DOMAINS.items():
    s = kb_stats(key)
    # Internal Slack threads are not shown to partners, so they are left out of these counts.
    by_source = {k: v for k, v in s["by_source"].items() if k != "slack"}
    rows.append({"Domain": d["label"], "Official doc pages": s["doc_pages"],
                 "Doc chunks": by_source.get("doc", 0),
                 "API-spec chunks": by_source.get("api_spec", 0),
                 "Past cases (synthetic)": by_source.get("ticket", 0),
                 "Total chunks": sum(by_source.values())})
table(pd.DataFrame(rows))
st.markdown("""
| Source | Description | Trust level |
|---|---|---|
| [Singpass Developer Docs](https://docs.developer.singpass.gov.sg/docs) | Public docs: Login, Myinfo, FAPI 2.0 specifications, migration guides, Developer Portal, Sign | Official |
| [Corppass Docs](https://docs.corppass.gov.sg) | Public docs: Corppass Login, Myinfo Business, Authorization API (FAPI 2.0), CDP user guide, FAQs | Official |
| Myinfo OpenAPI spec | Person and Entity data schemas | Official |
| Zendesk-style tickets | Fictional cases grounded in documented error codes, FAQs and migration guides | Synthetic, for illustration |
""")

st.markdown("### Features")
table(pd.DataFrame([
    ("💬 Ask the Assistant", "Chat in natural language with cited answers, follow-up suggestions, source "
                            "filters and a support-request draft",
     "Text, chat, expandable sources"),
    ("🩺 Integration Troubleshooter", "Form-based diagnosis: likely causes ranked by likelihood, a fix checklist, "
                                     "how others resolved similar issues, and when to contact support",
     "Interactive form, checklist, table"),
    ("🗺️ Integration Planner", "Onboarding or migration plan tailored to the partner's scenario, with a progress "
                              "tracker, data-attribute table and plan Q&A", "Form, tabs, checklist, table, chat"),
    ("📊 Knowledge Insights", "Common issues and past resolutions, a searchable Myinfo data catalogue and KB "
                             "coverage",
                             "KPI tiles, charts, searchable tables"),
    ("🧭 Personalisation", "Optional non-PII context about your integration that tailors every answer",
     "Sidebar form"),
    ("🛡️ Guardrails", "Automatic redaction of PII and secrets, prompt-injection filtering, grounded-only answers",
                     "Inline notices"),
], columns=["Feature", "What it does", "Formats"]))

st.markdown("""
### Limitations & disclaimer
- Answers are AI-generated and can be wrong. Check them against the cited official documentation before
  acting on them or sending them to anyone.
- Historical cases are synthetic. In a production rollout they would come from sanitised Zendesk exports.
- The knowledge base is a snapshot of the documentation taken when it was ingested. Re-run ingestion to
  pick up documentation changes.
- Do not enter personal data, credentials or production tokens. Anything detected is redacted automatically,
  but redaction is a safety net, not a guarantee.
""")
