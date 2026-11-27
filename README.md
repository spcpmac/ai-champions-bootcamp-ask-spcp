# Ask Singpass: Better Partner Support Helper (POC)

A password-protected Streamlit app that lets Singpass and Corppass partners help themselves with integration
questions, with a **support officer mode** (sidebar toggle) for internal staff. It uses an LLM with RAG over the official developer docs, the Myinfo API spec and historical cases
(synthetic in this POC).

**Domains** (switch in the sidebar; each has its own knowledge base): Singpass / Myinfo · Corppass / Myinfo Business

| Page | Use case |
|---|---|
| 💬 Ask the Assistant | Chat with cited answers, follow-up suggestions, and a support-request draft (partner) or partner-reply draft (officer) |
| 🩺 Integration Troubleshooter | Form → ranked causes, fix checklist, contact-support / escalation advice, how others resolved it |
| 🗺️ Integration Planner | Personalised onboarding or migration checklist, data-attribute table, plan Q&A |
| 📊 Knowledge Insights | Case dashboards, Myinfo data catalogue, KB coverage |
| ℹ️ About Us · 🧪 Methodology | Required documentation pages (Methodology has one flowchart per use case) |

## Setup
```bash
uv venv --python 3.11 .venv && uv pip install --python .venv/bin/python -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml   # set APP_PASSWORD and OPENAI_API_KEY
```

## Build the knowledge bases (each domain independently)
```bash
export OPENAI_API_KEY=sk-...                      # or rely on secrets.toml
python scripts/fetch_docs.py   --domain singpass  # optional: refresh doc snapshot (already in data/raw)
python scripts/seed_synthetic.py                  # synthetic tickets + Slack (already in data/synthetic)
python scripts/ingest.py --domain singpass        # → data/chroma, collection kb_singpass
python scripts/ingest.py --domain corppass        # → data/chroma, collection kb_corppass
python scripts/eval.py   --domain singpass --judge   # optional: retrieval hit@k + faithfulness
```
`ingest.py --dry-run` only chunks the content, writing `data/chunks/<domain>.jsonl` for inspection. No API key is needed.
`generate_synthetic.py --domain X --n 20` adds more LLM-generated synthetic tickets grounded in doc sections.

## Run
```bash
streamlit run streamlit_app.py
```

## Deploy (Streamlit Community Cloud)
1. Commit everything, **including `data/chroma/`**. The app only reads the index at runtime and never re-embeds.
2. Create the app with main file `streamlit_app.py` and Python 3.11.
3. Under **Secrets**, add `APP_PASSWORD`, `OPENAI_API_KEY` and optionally `OPENAI_CHAT_MODEL`.

`pysqlite3-binary` gets installed on Linux, and `streamlit_app.py` swaps it in for Cloud's old sqlite3, which Chroma can't use.

## Layout
```
streamlit_app.py      entry: password gate, sidebar, navigation
app_pages/            one file per page
core/                 config, auth, llm, chunking, retriever, prompts, guardrails, ui, catalogue
scripts/              fetch_docs, seed_synthetic, generate_synthetic, ingest, eval
data/raw/             doc snapshots (GitBook llms-full.txt + llms.txt index)
data/synthetic/       synthetic tickets & Slack threads (JSONL)
data/eval/            golden questions + results.json
data/chroma/          persisted vector store (built by ingest.py)
```
