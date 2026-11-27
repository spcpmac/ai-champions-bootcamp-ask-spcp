"""Simple shared-password gate (pattern from Streamlit docs)."""
from __future__ import annotations

import hmac

import streamlit as st

from core.config import APP_NAME, get_setting


def check_password() -> bool:
    """Return True once the user has entered the correct password."""
    if st.session_state.get("password_correct"):
        return True

    expected = get_setting("APP_PASSWORD")
    if not expected:
        st.error("APP_PASSWORD is not configured. Add it to `.streamlit/secrets.toml` "
                 "or the Streamlit Cloud secrets.")
        return False

    def _submit():
        entered = st.session_state.pop("password", "")
        st.session_state["password_correct"] = hmac.compare_digest(
            entered.encode(), expected.encode()
        )
        st.session_state["password_attempted"] = True

    st.title(f"🔐 {APP_NAME}")
    st.caption("Self-service integration help for Singpass & Corppass partners. Prototype for educational purposes.")
    st.text_input("Password", type="password", key="password", on_change=_submit)
    if st.session_state.get("password_attempted") and not st.session_state.get("password_correct"):
        st.error("😕 Incorrect password")
    return False
