"""Methodology — data flows, implementation details and one flowchart per use case."""
from __future__ import annotations

import json

import pandas as pd
import streamlit as st

from core.config import (APP_NAME, CHUNK_OVERLAP_TOKENS, CHUNK_TOKENS, EVAL_DIR, FINAL_K, MMR_LAMBDA, RETRIEVE_K,
                         chat_model, embed_model)
from core.ui import table

st.title("🧪 Methodology")
st.caption(f"How data flows through {APP_NAME}, and how each use case works.")

NODE = 'node [shape=box style="rounded,filled" fillcolor="#eef4fc" color="#257de0" fontname="Helvetica" fontsize=11];'
EDGE = 'edge [color="#666666" fontname="Helvetica" fontsize=9];'


def flow(body: str, rankdir: str = "TB") -> None:
    st.graphviz_chart(f"digraph {{ rankdir={rankdir}; bgcolor=transparent; {NODE} {EDGE} {body} }}",
                      width="stretch")


DEC = 'shape=diamond style=filled fillcolor="#fff4e5" color="#f2a600"'
LLM = 'fillcolor="#efeafd" color="#6a4ce2"'
IO = 'shape=parallelogram fillcolor="#e8f7f2" color="#00b894"'

st.header("1. Data flow overview")
st.markdown("""
The system has two pipelines. **Offline ingestion** builds a separate knowledge base for each domain.
**Online serving** answers partners' questions using retrieval-augmented generation (RAG).
""")
st.subheader("1a. Offline ingestion (run once per domain: `scripts/ingest.py --domain …`)")
flow(f"""
docs [label="Official docs\\n(GitBook llms-full.txt)" {IO}];
spec [label="Myinfo OpenAPI spec" {IO}];
tix  [label="Synthetic Zendesk tickets\\n+ Slack threads (JSONL)" {IO}];
clean [label="Clean\\n• strip LLM-directed preamble\\n• HTML tables → markdown\\n• drop images / nav"];
split [label="Split into pages (H1, fence-aware)\\nmap page → source URL via llms.txt"];
chunk [label="Heading-aware chunking\\n~{CHUNK_TOKENS} tokens, {CHUNK_OVERLAP_TOKENS} overlap\\ntables & code kept whole"];
meta [label="Metadata\\ndomain · source_type · product\\ntitle · section · url · error_codes"];
emb [label="Embed\\n{embed_model()}" {LLM}];
db [label="Chroma collection\\nkb_singpass | kb_corppass" shape=cylinder fillcolor="#e8f7f2" color="#00b894"];
docs -> clean -> split -> chunk; spec -> chunk; tix -> chunk; chunk -> meta -> emb -> db;
""", "LR")

st.subheader("1b. Online serving (shared by every use case)")
flow(f"""
u [label="Partner input\\n(chat / form)" {IO}];
pw [label="Password gate" {DEC}];
g [label="Guardrails\\nredact NRIC/UEN/email/phone\\nJWT/keys/secrets · injection check"];
dom [label="Domain switcher → collection\\nAllowed sources\\n(no Slack, no ticket IDs)"];
r [label="Retrieve\\nembed query → top-{RETRIEVE_K}\\nmetadata filter → MMR → {FINAL_K}"];
f [label="Context filter\\n(drop instruction-like chunks)"];
p [label="Prompt\\nsystem rules + integration context\\n+ numbered <source> blocks"];
l [label="LLM\\n{chat_model()}" {LLM}];
o [label="Answer with citations\\n+ sources, tables, charts" {IO}];
u -> pw -> g -> dom -> r -> f -> p -> l -> o;
""", "LR")

st.header("2. Use-case flowcharts")
uc1, uc2, uc3, uc4 = st.tabs(["UC1 · Ask the Assistant", "UC2 · Troubleshooter", "UC3 · Integration Planner",
                              "UC4 · Knowledge Insights"])

with uc1:
    st.markdown("Conversational Q&A with citations and follow-up questions. Partners can draft a support request.")
    flow(f"""
    q [label="User asks a question\\n(or picks a suggested follow-up)" {IO}];
    s [label="Scrub PII / secrets"];
    inj [label="Injection attempt?" {DEC}];
    ref [label="Polite refusal" {IO}];
    h [label="Chat history\\nexists?" {DEC}];
    rw [label="Rewrite into a\\nstandalone query" {LLM}];
    rt [label="Retrieve from the source types\\nselected by the user"];
    gen [label="Generate grounded answer\\nwith [n] citations + 3 follow-ups (streamed)" {LLM}];
    show [label="Show answer, sources,\\nfollow-up chips" {IO}];
    d [label="Draft\\nrequested?" {DEC}];
    sr [label="Support request draft\\n(placeholders, no secrets)" {LLM}];
    q -> s -> inj; inj -> ref [label="yes"]; inj -> h [label="no"];
    h -> rw [label="yes"]; h -> rt [label="no"]; rw -> rt -> gen -> show -> d;
    d -> sr [label="yes"]; show -> q [label="follow-up" style=dashed];
    """)

with uc2:
    st.markdown("A structured form turns a failing integration into a ranked diagnosis, a fix checklist and "
                "similar past cases, plus advice on when to contact partner support.")
    flow(f"""
    f [label="Form: product, failing step, error code,\\nHTTP status, environment, stack, details" {IO}];
    s [label="Scrub pasted logs"];
    q [label="Compose search query"];
    r1 [label="Retrieve official docs + spec\\n(error-code boosted)"];
    r2 [label="Retrieve similar past cases"];
    llm [label="Structured diagnosis (JSON schema)\\ncauses · fixes · details to check · needs support?" {LLM}];
    esc [label="Needs\\nsupport?" {DEC}];
    w [label="'Contact partner support'" {IO}];
    ok [label="Show 'fixable on\\nyour side'" {IO}];
    out [label="Ranked causes · interactive fix checklist\\n· how others resolved it · sources" {IO}];
    sr [label="Draft support\\nrequest from form + diagnosis" {LLM}];
    f -> s -> q; q -> r1; q -> r2; r1 -> llm; r2 -> llm; llm -> esc;
    esc -> w [label="yes"]; esc -> ok [label="no"]; w -> out; ok -> out; out -> sr [label="still stuck" style=dashed];
    """)

with uc3:
    st.markdown("A personalised onboarding or migration plan based on the partner's non-identifying profile.")
    flow(f"""
    f [label="Form: product, scenario (new / v3→v5 …),\\napp type, stage, Myinfo data needed" {IO}];
    ctx [label="Merge with sidebar\\npartner context"];
    r [label="Retrieve: requirements (docs)\\n+ data attributes (spec)\\n+ pitfalls (tickets)"];
    llm [label="Structured plan (JSON schema)\\nPrepare → Build → Test → Go-live" {LLM}];
    ui [label="Phase tabs with checkboxes + progress bar\\nselected-data table · pitfalls · sources" {IO}];
    fq [label="Follow-up question\\nabout the plan" {IO}];
    a [label="Answer grounded in plan\\n+ fresh retrieval" {LLM}];
    f -> ctx -> r -> llm -> ui -> fq -> a -> ui;
    """)

with uc4:
    st.markdown("Dashboards over historical cases and the knowledge base. This page makes no LLM calls; everything is computed directly from the data.")
    flow(f"""
    src [label="Synthetic past cases (JSONL)\\nMyinfo OpenAPI spec\\nChroma metadata" {IO}];
    load [label="Load + cache\\n(pandas, st.cache_data)"];
    flt [label="Filters: product,\\nenvironment, date range" {IO}];
    agg [label="Aggregate\\ncounts · medians"];
    viz [label="KPI tiles + Plotly charts\\n(category, error codes, trend, resolution time)" {IO}];
    tbl [label="Searchable case log\\n+ case detail view" {IO}];
    cat [label="Searchable data catalogue\\n+ KB coverage charts" {IO}];
    src -> load -> flt -> agg; agg -> viz; agg -> tbl; load -> cat;
    """)

st.header("3. Implementation details")
table(pd.DataFrame([
    ("Frontend", "Streamlit multipage app (st.navigation); password-protected; sidebar domain switcher"),
    ("Audience", "Partner self-service only. Internal Slack threads and ticket IDs are never shown, and "
                 "prompts hide internal IDs"),
    ("LLM", f"OpenAI {chat_model()} (configurable via OPENAI_CHAT_MODEL); streaming for chat; "
            "Pydantic structured outputs for the Troubleshooter and Planner"),
    ("Embeddings", f"OpenAI {embed_model()}"),
    ("Vector store", "ChromaDB (persistent, cosine), one collection per domain, built offline and committed"),
    ("Chunking", f"~{CHUNK_TOKENS} tokens, {CHUNK_OVERLAP_TOKENS} overlap; split at H1 then H2; "
                 "tables/code atomic; oversized tables split by row with header repeated"),
    ("Retrieval", f"top-{RETRIEVE_K} cosine → MMR (λ={MMR_LAMBDA}) → {FINAL_K}; metadata filter on source_type; "
                  "error-code boosting; history-aware query rewriting"),
    ("Grounding", "Numbered <source> blocks; answer only from sources; inline [n] citations; "
                  "official docs take priority over precedent cases"),
    ("Guardrails", "Regex redaction (NRIC/FIN, UEN, email, phone, JWT, PEM keys, JWK private params, secrets); "
                   "prompt-injection filter on input and retrieved context; out-of-scope refusal; disclaimer"),
    ("Personalisation", "Non-PII partner context (partner type, app type, stack, environment, experience) "
                        "injected into prompts"),
], columns=["Component", "Approach"]))

st.header("4. Evaluation")
res_path = EVAL_DIR / "results.json"
if res_path.exists():
    res = json.loads(res_path.read_text())
    st.markdown("Results of `scripts/eval.py` on hand-written golden questions (retrieval hit@k = whether the "
                "expected doc page appears among the retrieved chunks).")
    table(pd.DataFrame(res))
else:
    st.info("Run `python scripts/eval.py --domain singpass` and `--domain corppass` to populate evaluation results.")
