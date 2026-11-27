"""Thin wrapper around the OpenAI SDK: chat, streaming, structured output, embeddings."""
from __future__ import annotations

from functools import lru_cache
from typing import Iterator, TypeVar

from openai import OpenAI
from pydantic import BaseModel

from core.config import chat_model, embed_model, get_setting

T = TypeVar("T", bound=BaseModel)


@lru_cache(maxsize=1)
def client() -> OpenAI:
    key = get_setting("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY is not configured (secrets.toml or environment).")
    return OpenAI(api_key=key)


def chat(messages: list[dict], model: str | None = None, **kw) -> str:
    resp = client().chat.completions.create(model=model or chat_model(), messages=messages, **kw)
    return resp.choices[0].message.content or ""


def chat_stream(messages: list[dict], model: str | None = None) -> Iterator[str]:
    stream = client().chat.completions.create(
        model=model or chat_model(), messages=messages, stream=True
    )
    for event in stream:
        if event.choices and event.choices[0].delta.content:
            yield event.choices[0].delta.content


def chat_structured(messages: list[dict], schema: type[T], model: str | None = None) -> T:
    resp = client().chat.completions.parse(
        model=model or chat_model(), messages=messages, response_format=schema
    )
    parsed = resp.choices[0].message.parsed
    if parsed is None:
        raise RuntimeError(resp.choices[0].message.refusal or "Model returned no structured output.")
    return parsed


def embed(texts: list[str], batch_size: int = 128) -> list[list[float]]:
    out: list[list[float]] = []
    for i in range(0, len(texts), batch_size):
        batch = [t.replace("\n", " ")[:24000] for t in texts[i : i + batch_size]]
        resp = client().embeddings.create(model=embed_model(), input=batch)
        out.extend(d.embedding for d in resp.data)
    return out
