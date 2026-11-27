"""Ask Singpass: Better Partner Support Helper — entry point.

Run locally:  streamlit run streamlit_app.py
"""
# Streamlit Community Cloud ships an old sqlite3; Chroma needs >= 3.35.
try:  # pragma: no cover
    __import__("pysqlite3")
    import sys

    sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
except ImportError:
    pass

import streamlit as st

from core.auth import check_password
from core.config import APP_NAME
from core.ui import apply_style, sidebar

st.set_page_config(page_title=APP_NAME, page_icon="🛡️", layout="wide")
apply_style()

if not check_password():
    st.stop()

sidebar()

pages = {
    "Use cases": [
        st.Page("app_pages/assistant.py", title="Ask the Assistant", icon="💬", default=True),
        st.Page("app_pages/troubleshooter.py", title="Integration Troubleshooter", icon="🩺"),
        st.Page("app_pages/planner.py", title="Integration Planner", icon="🗺️"),
        st.Page("app_pages/insights.py", title="Knowledge Insights", icon="📊"),
    ],
    "About": [
        st.Page("app_pages/about_us.py", title="About Us", icon="ℹ️"),
        st.Page("app_pages/methodology.py", title="Methodology", icon="🧪"),
    ],
}
st.navigation(pages).run()
