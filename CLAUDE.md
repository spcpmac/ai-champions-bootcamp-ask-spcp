# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

This is a proof of concept for an AI Bootcamp project. It is a password-protected Streamlit app that serves as an LLM + RAG self-service assistant, "Ask Singpass: Better Partner Support Helper" (`APP_NAME` in `core/config.py`), for Singpass/Myinfo and Corppass/Myinfo Business partner-integration support. The requirements are in `ref/problem-statement.md`. They mandate an **About Us** page and a **Methodology** page, and the Methodology page must have **one flowchart per use case**. Keep those pages in sync when you add or change a use case.

## Current status (deployed)

- **Live:** deployed on Streamlit Community Cloud from GitHub repo `spcpmac/ai-champions-bootcamp-ask-spcp`, branch `main`, main file `streamlit_app.py`, Python 3.14. **Every push to `main` redeploys the live app**, so run the smoke test before pushing.
- **Cloud secrets:** set in the Cloud app's Settings → Secrets as top-level TOML keys (`APP_PASSWORD`, `OPENAI_API_KEY`, `OPENAI_CHAT_MODEL = "gpt-6-luna"`), with no `[section]` header. If you see "APP_PASSWORD is not configured", the Cloud secrets are missing or the TOML is invalid.
- **Latest eval** (`data/eval/results.json`, gpt-6-luna): Singpass hit@6 100%, MRR 0.85, faithfulness 77%; Corppass hit@6 100%, MRR 0.80, faithfulness 100%. Singpass faithfulness is judge-noisy. Its known weak spot is the "Migrate Myinfo v3" golden question, where the MIB Person-v3 guide outranks the v3 guide; making that question more specific is an open option.

## Git and publishing

- Push over **HTTPS with the user's personal GitHub account** (`gh auth login`). **Never use the work SSH keys or work email.** The repo-local `git config user.email` is a GitHub noreply address, while the global git email is a work address, so never pass `--global` or override it.
- The Claude Code sandbox blocks writes inside `.git/`, so `git add/commit/push` must run with the sandbox disabled. Only commit or push when the user asks.
- Opening the Chroma index, including in tests, rewrites `data/chroma/chroma.sqlite3` and `data_level0.bin`. Revert them with `git checkout -- data/chroma` unless you deliberately re-ingested.

## Commands

The venv is Python 3.14 at `.venv/`; Streamlit Cloud targets 3.14 (chosen in the app's Advanced settings; Cloud ignores runtime.txt). Prefix commands with `.venv/bin/`.

```bash
uv venv --python 3.14 .venv && uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/streamlit run streamlit_app.py

.venv/bin/python scripts/ingest.py --domain singpass|corppass [--dry-run]
.venv/bin/python scripts/eval.py --domain singpass|corppass [--judge]
.venv/bin/python scripts/seed_synthetic.py
.venv/bin/python scripts/generate_synthetic.py --domain X --n 20
.venv/bin/python scripts/fetch_docs.py --domain X
```

- `streamlit run` reads secrets from `.streamlit/secrets.toml`, which is gitignored; the template is `secrets.toml.example`. It needs `APP_PASSWORD` and `OPENAI_API_KEY`, and optionally `OPENAI_CHAT_MODEL` / `OPENAI_EMBED_MODEL`. `core.config.get_setting` falls back to environment variables, so the scripts work with just `export OPENAI_API_KEY=...`.
- `ingest.py` rebuilds only that domain's Chroma collection in `data/chroma/`. It always writes `data/chunks/<domain>.jsonl`. With `--dry-run` it skips embedding, so no API key is needed; use this to inspect chunking.
- `eval.py` measures retrieval hit@k/MRR against the golden questions in `data/eval/<domain>.json`. `--judge` adds an LLM faithfulness score. Results merge into `data/eval/results.json`, which the Methodology page displays.
- `seed_synthetic.py` regenerates the hand-authored synthetic tickets and Slack threads deterministically (seed 42).
- `generate_synthetic.py` appends LLM-generated synthetic tickets grounded in doc chunks. Run an ingest first so the chunks exist.
- `fetch_docs.py` refreshes the GitBook doc snapshot in `data/raw/<domain>/`. It follows "Next part" pagination and downloads `llms.txt`.
- tiktoken downloads its encoding on first use. Set `TIKTOKEN_CACHE_DIR=$PWD/.cache/tiktoken` to cache it locally.
- There is no test suite or linter configured. Verify UI changes headlessly with `streamlit.testing.v1.AppTest`:
  1. Run with `APP_PASSWORD`/`OPENAI_API_KEY` env vars set.
  2. Enter the password via `at.text_input(key="password")`.
  3. Visit each page with `at.switch_page("app_pages/<page>.py")` and check `at.exception`.

  The LLM-backed paths can be exercised without a key: monkeypatch `core.llm.chat`, `core.llm.chat_stream`, `core.llm.chat_structured` and `core.retriever.embed`, then point `core.retriever.CHROMA_DIR` at a temp index.

## Architecture

**One engine, two domains.** Everything domain-specific is in `core/config.py: DOMAINS`. That covers the Chroma collection name, raw-doc directory, product list, error codes, scenarios, OpenAPI schema (`Person` for Singpass, `Entity` for Corppass), scope hint and sample questions. The sidebar `st.radio(key="domain")` in `core/ui.py` sets `st.session_state.domain`. Every page reads `cfg()` / `domain()`, and per-domain state is keyed by domain (`history[domain]`, and `diag_{domain}` / `plan_{domain}`). To add a domain, add a `DOMAINS` entry, `data/raw/<domain>/`, synthetic JSONL and eval JSON; no page code should need changes.

**Partner-only.** The app is for integrating partners only; there is no support-officer mode. Slack threads are ingested but never shown: the Assistant's source filter uses `core/ui.SOURCE_LABELS` (doc, api_spec, ticket), and Insights and About Us leave Slack out of their counts. `format_context()` always hides ticket IDs, and `render_sources` does the same. Drafts are support requests (`support_request_system`).

**Offline ingestion** runs `scripts/ingest.py`, which calls the pure functions in `core/chunking.py`:
1. **Page split:** the raw docs are GitBook `llms-full.txt` exports, possibly multi-part (`part1.md`…). `split_gitbook_pages` splits them into pages at `# ` H1, skipping code fences, since doc code blocks contain `# comments`.
2. **URL mapping:** each page is mapped to its source URL by walking the ordered `llms.txt` index (`parse_index`).
3. **Strip LLM-directed text:** the exports contain an "Agent Instructions" preamble and pagination footers that address LLMs. These are stripped, and `guardrails.filter_context` also drops instruction-like chunks at query time.
4. **Clean and chunk:** `clean_markdown` converts raw HTML `<table>` to markdown tables; that is where parameter and error-code details live. Markdownify escaping must stay off, or `invalid_dpop_proof` becomes `invalid\_dpop\_proof` and breaks search and error-code tagging. `chunk_page` packs blocks into chunks of ~`CHUNK_TOKENS`, keeps tables and code atomic, prefers H2 boundaries, and prefixes each chunk with a `[Parents > Page > Section]` breadcrumb. `url_parents` derives the parents from the URL path, which is what disambiguates near-duplicate pages such as the v3 and v4 migration guides. Breadcrumb changes need a re-ingest.
5. **Metadata and storage:** each chunk carries `domain, source_type (doc|ticket|slack|api_spec), product, title, section, url, error_codes (comma-joined string), synthetic`. Chroma metadata must be scalar. Collections are created with `embedding_function=None`; embeddings always come from `core.llm.embed` (OpenAI).

**Online serving:**
- **Entry:** `streamlit_app.py` swaps in `pysqlite3` (Streamlit Cloud's sqlite is too old for Chroma), applies the `core/auth.check_password` gate, then renders the sidebar and `st.navigation` over `app_pages/`.
- **Shared RAG pattern (UC1–UC3):**
  1. `guardrails.scrub()` the user text.
  2. `retriever.retrieve(domain, query, source_types=[...], error_code=...)` runs the Chroma query on the OpenAI query embedding (top `RETRIEVE_K`). Before MMR it re-weights relevance: legacy-spec chunks (`/legacy-` in the URL, e.g. Myinfo v3/v4 and pre-FAPI 2.0) are demoted unless the question mentions legacy/v3/v4/pre-FAPI, and chunks tagged with the error code (from the form or detected in the query) are boosted. Legacy sources are labelled `LEGACY spec` in the prompt context.
  3. `retriever.format_context()` produces numbered `<source id=n>` blocks.
  4. Prompts come from `core/prompts.py`; all of them share `BASE_RULES`: answer only from sources, cite `[n]`, treat sources as data.
  5. `core/ui.profile_text()` injects the optional non-PII partner context from the sidebar.
- **Per page:**
  - The Assistant (`assistant.py`) streams via `llm.chat_stream`. It rewrites follow-ups into standalone queries and parses a trailing `**Follow-ups:**` list into `st.pills` chips via `ui.suggestion_chips`. When the chat is empty, `st.chat_input` sits inside a container so it renders inline under the welcome text. Once history exists it sits at the top level, which pins it to the bottom of the window.
  - The Troubleshooter and Planner use `llm.chat_structured` with the Pydantic schemas in `prompts.py` (`Diagnosis`, `IntegrationPlan`).
  - Insights (`insights.py`) makes no LLM calls. It uses `core/catalogue.py`: synthetic JSONL via pandas, and the Myinfo catalogue from `ref/openapi.yaml`.
- **Lazy heavy imports:** `core/chunking.py` imports tiktoken/bs4/markdownify lazily because the app imports `catalogue_rows` from it at runtime; keep it that way.

**Data conventions:**
- Tickets and Slack threads in `data/synthetic/` are fictional and must stay marked `synthetic: true`. The UI labels them as synthetic.
- Official docs outrank tickets in prompts.
- `data/chroma/` is committed and read-only at runtime. The deployed app never embeds documents; it only embeds queries.

**Layout:** `ui.apply_style()` injects compact CSS. `.block-container` top padding must stay above Streamlit's fixed 3.75rem header, or page titles get clipped; it is currently 4.25rem. Each page starts with `ui.page_header()`, which shows the domain and a caption. The Assistant puts `⚙️ Sources` (popover) and `🧹 New chat` in a bottom-aligned header row and shows the collapsed `ui.important_notice()` disclaimer.

**Charts** (Insights): use single-series Plotly bars/lines in one hue (`#257de0`), via the `style()` helper. Don't use legends or dual axes, and pair charts with a table view. Methodology flowcharts use built-in `st.graphviz_chart` (DOT), not Mermaid, to avoid extra components on Streamlit Cloud. Their SVG is capped at 900px wide in `ui.apply_style()`, so they don't fill very large screens.

**Tables:** use `ui.table(df, labels=, formats=)` for read-only tables, not `st.dataframe`. `st.dataframe` truncates long cell text and Streamlit 1.67 can't wrap it. `table()` renders wrapping HTML and escapes cell content. Because of this, table columns can't be sorted by clicking headers. Markdown tables are styled to wrap too.
