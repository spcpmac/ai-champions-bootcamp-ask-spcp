"""UC1 — Ask the Assistant: conversational RAG with citations, follow-ups and drafting.

Partner mode (default): self-service answers and a "draft support request" helper.
Support officer mode: internal sources visible and a "draft partner reply" helper.
"""
from __future__ import annotations

import re

import streamlit as st

from core import llm
from core.guardrails import looks_like_injection, scrub
from core.prompts import REWRITE_SYSTEM, assistant_system, reply_draft_system, support_request_system
from core.retriever import format_context, retrieve
from core.ui import (audience, cfg, domain, important_notice, is_officer, page_header, profile_text,
                     redaction_notice, render_sources, require_kb, source_options, suggestion_chips)

c = cfg()
officer = is_officer()
histories = st.session_state.setdefault("history", {})
history: list[dict] = histories.setdefault(domain(), [])
opts = source_options()

# ---- header row: title on the left, compact toolbar on the right (bottom-aligned)
head, b1, b2 = st.columns([6, 1.2, 1.2], vertical_alignment="bottom")
with head:
    page_header("💬 Ask the Assistant", "Ask in plain language and get cited answers")
with b1.popover("⚙️ Sources", width="stretch"):
    sources = st.multiselect("Search in", list(opts), default=list(opts), format_func=opts.get,
                             key=f"src_{domain()}_{audience()}")
if b2.button("🧹 New chat", width="stretch", disabled=not history):
    history.clear()
    st.rerun()
important_notice()
if not require_kb():
    st.stop()


def ask(q: str) -> None:
    st.session_state["pending_q"] = q


def split_followups(answer: str) -> tuple[str, list[str]]:
    m = re.search(r"\*\*Follow-ups:?\*\*:?", answer)
    if not m:
        return answer, []
    body, tail = answer[: m.start()].rstrip(), answer[m.end():]
    qs = [re.sub(r"^\s*[-*\d.]+\s*", "", l).strip() for l in tail.splitlines() if l.strip()]
    return body, [q for q in qs if q][:3]


def draft(idx: int) -> None:
    msg = history[idx]
    question = history[idx - 1]["content"] if idx > 0 else ""
    links = sorted({h["metadata"]["url"] for h in msg["hits"]
                    if h["metadata"].get("url") and h["metadata"]["source_type"] == "doc"})
    convo = "\n".join(f"{m['role']}: {m['content'][:800]}" for m in history[: idx + 1][-6:])
    if officer:
        system, user = reply_draft_system(c["label"]), (
            f"Partner question:\n{question}\n\nVerified answer:\n{msg['content']}\n\n"
            "Official documentation links:\n" + "\n".join(links))
    else:
        system, user = support_request_system(c["label"]), (
            f"Partner context: {profile_text() or 'not provided'}\n\nConversation so far:\n{convo}\n\n"
            "Relevant documentation already consulted:\n" + "\n".join(links))
    with st.spinner("Drafting…"):
        msg["draft"] = llm.chat([{"role": "system", "content": system}, {"role": "user", "content": user}])
        msg["draft_kind"] = audience()


# ---- empty state
if not history:
    st.markdown(f"Hi! Ask me anything about integrating with **{c['label']}**: flows, error codes, keys "
                "and JWKS, Myinfo data, migrations, or the developer portal."
                + ("" if officer else " Add details under **About your integration** in the sidebar "
                                      "for answers tailored to your setup."))
    suggestion_chips(c["sample_questions"], f"chips_start_{domain()}", ask, "Try asking")

# ---- conversation
draft_label = "✉️ Draft partner reply" if officer else "📨 Draft a support request"
for i, msg in enumerate(history):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("redacted"):
            st.caption(f"🛡️ Redacted {msg['redacted']} before sending to the AI model.")
        if msg["role"] != "assistant" or not msg.get("hits"):
            continue
        render_sources(msg["hits"])
        if st.button(draft_label, key=f"draft_{domain()}_{audience()}_{i}", type="tertiary"):
            draft(i)
        if msg.get("draft") and msg.get("draft_kind") == audience():
            title = ("✉️ Draft reply: review and edit before sending" if officer
                     else "📨 Support request draft: remove anything sensitive before sending")
            with st.expander(title, expanded=True):
                st.code(msg["draft"], language="markdown", wrap_lines=True)

if history and history[-1]["role"] == "assistant":
    suggestion_chips(history[-1].get("followups", []), f"chips_{domain()}_{len(history)}", ask,
                     "Suggested follow-ups")

# Empty chat: show the input inline under the welcome text so it isn't stranded at the bottom of the
# screen. Once a conversation exists, use the standard chat layout with the input pinned to the bottom.
placeholder = f"Ask about {c['short']} integration…"
if history:
    typed = st.chat_input(placeholder, key="chat_input")
else:
    with st.container():
        typed = st.chat_input(placeholder, key="chat_input_start")
prompt = typed or st.session_state.pop("pending_q", None)
if not prompt:
    st.stop()

# ---- handle a new question
clean = scrub(prompt)
with st.chat_message("user"):
    st.markdown(clean.text)
redaction_notice(clean)
history.append({"role": "user", "content": clean.text, "redacted": clean.summary()})

with st.chat_message("assistant"):
    if looks_like_injection(clean.text):
        answer = "I can only help with integration questions, and I can't change my instructions."
        st.markdown(answer)
        history.append({"role": "assistant", "content": answer, "hits": []})
        st.stop()

    with st.status("Searching the knowledge base…", expanded=False) as status:
        query = clean.text
        if len(history) > 1:
            convo = "\n".join(f"{m['role']}: {m['content'][:600]}" for m in history[-7:-1])
            query = llm.chat([{"role": "system", "content": REWRITE_SYSTEM},
                              {"role": "user", "content": f"History:\n{convo}\n\nLatest: {clean.text}"}]).strip()
        st.write(f"🔎 Search query: `{query}`")
        hits = retrieve(domain(), query, source_types=sources or list(opts))
        status.update(label=f"Found {len(hits)} relevant sources", state="complete")

    messages = [{"role": "system",
                 "content": assistant_system(c["label"], c["scope_hint"], profile_text(), audience())}]
    for m in history[-7:-1]:
        messages.append({"role": m["role"], "content": m["content"]})
    messages.append({"role": "user", "content": f"<sources>\n{format_context(hits, public=not officer)}\n"
                                                f"</sources>\n\nQuestion: {clean.text}"})
    raw = st.write_stream(llm.chat_stream(messages))
    body, followups = split_followups(raw if isinstance(raw, str) else "".join(raw))
    history.append({"role": "assistant", "content": body, "hits": hits, "followups": followups})
    st.rerun()
