"""Loaders for structured data shown in tables/charts (Myinfo spec, synthetic tickets)."""
from __future__ import annotations

import json

import pandas as pd
import streamlit as st
import yaml

from core.chunking import catalogue_rows
from core.config import DOMAINS, OPENAPI_PATH, SYNTHETIC_DIR


@st.cache_data(show_spinner=False)
def data_catalogue(domain: str) -> pd.DataFrame:
    spec = yaml.safe_load(OPENAPI_PATH.read_text())
    return pd.DataFrame(catalogue_rows(spec, DOMAINS[domain]["openapi_schema"]))


@st.cache_data(show_spinner=False)
def tickets(domain: str) -> pd.DataFrame:
    path = SYNTHETIC_DIR / f"{domain}_tickets.jsonl"
    if not path.exists():
        return pd.DataFrame()
    df = pd.DataFrame([json.loads(l) for l in path.read_text().splitlines() if l.strip()])
    df["created_at"] = pd.to_datetime(df["created_at"])
    df["error_code"] = df["error_code"].fillna("(none)")
    return df
