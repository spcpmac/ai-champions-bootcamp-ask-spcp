"""UC4 — Knowledge Insights: dashboards over historical cases + Myinfo data catalogue + KB coverage."""
from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from core.catalogue import data_catalogue, slack, tickets
from core.config import SOURCE_TYPES
from core.retriever import kb_stats
from core.ui import cfg, domain, is_officer, page_header

SERIES = "#257de0"   # single-series hue (validated reference palette, slot 1)

page_header("📊 Knowledge Insights", "Common issues, the Myinfo data catalogue and knowledge-base coverage")
st.caption("Ticket and Slack data on this page is **synthetic**, for demonstration only.")
c = cfg()
df = tickets(domain())
officer = is_officer()


def style(fig, height=320):
    fig.update_traces(marker_color=SERIES, selector=dict(type="bar"))
    fig.update_traces(line=dict(color=SERIES, width=2), marker=dict(size=8, color=SERIES),
                      selector=dict(type="scatter"))
    fig.update_layout(height=height, margin=dict(l=8, r=8, t=8, b=8), bargap=0.35,
                      paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      xaxis=dict(showgrid=False), yaxis=dict(gridcolor="rgba(128,128,128,0.2)"),
                      hoverlabel=dict(font_size=13))
    return fig


tab_cases, tab_catalogue, tab_kb = st.tabs(["🎫 Historical cases" if officer else "🎫 Common issues", "🧩 Myinfo data catalogue", "📚 KB coverage"])

with tab_cases:
    if df.empty:
        st.info("No ticket data yet. Run `python scripts/seed_synthetic.py`.")
    else:
        f1, f2, f3 = st.columns([2, 2, 3])
        prods = f1.multiselect("Product", sorted(df["product"].unique()), placeholder="All products")
        envs = f2.multiselect("Environment", sorted(df["environment"].unique()), placeholder="All")
        lo, hi = df["created_at"].min().date(), df["created_at"].max().date()
        rng = f3.slider("Date range", min_value=lo, max_value=hi, value=(lo, hi), format="MMM YYYY")
        view = df[(df["created_at"].dt.date >= rng[0]) & (df["created_at"].dt.date <= rng[1])]
        if prods:
            view = view[view["product"].isin(prods)]
        if envs:
            view = view[view["environment"].isin(envs)]

        tiles = st.columns(4 if officer else 3)
        tiles[0].metric("Cases", len(view))
        tiles[1].metric("Median resolution", f"{view['resolution_time_hrs'].median():.0f} h" if len(view) else "—")
        tiles[2].metric("Distinct error codes", view.loc[view["error_code"] != "(none)", "error_code"].nunique())
        if officer:   # internal operational metric
            tiles[3].metric("Escalated to engineers",
                            f"{view['escalated_to_engineer'].mean():.0%}" if len(view) else "—")

        if view.empty:
            st.warning("No cases match the filters.")
        else:
            a, b = st.columns(2)
            with a:
                st.markdown("**Cases by category**")
                cat = view["category"].value_counts().sort_values().reset_index()
                st.plotly_chart(style(px.bar(cat, x="count", y="category", orientation="h",
                                             labels={"count": "Cases", "category": ""})),
                                width="stretch")
            with b:
                st.markdown("**Most common error codes**")
                err = view[view["error_code"] != "(none)"]["error_code"].value_counts().head(8) \
                    .sort_values().reset_index()
                st.plotly_chart(style(px.bar(err, x="count", y="error_code", orientation="h",
                                             labels={"count": "Cases", "error_code": ""})),
                                width="stretch")
            a, b = st.columns(2)
            with a:
                st.markdown("**Cases per month**")
                monthly = view.set_index("created_at").resample("MS").size().rename("cases").reset_index()
                st.plotly_chart(style(px.line(monthly, x="created_at", y="cases", markers=True,
                                              labels={"created_at": "", "cases": "Cases"})),
                                width="stretch")
            with b:
                st.markdown("**Median hours to resolve, by category**")
                med = view.groupby("category")["resolution_time_hrs"].median().sort_values().reset_index()
                st.plotly_chart(style(px.bar(med, x="resolution_time_hrs", y="category", orientation="h",
                                             labels={"resolution_time_hrs": "Median hours", "category": ""})),
                                width="stretch")

            st.markdown("**Case log**" if officer else "**Browse past resolved cases**")
            q = st.text_input("Filter cases", placeholder="keyword, e.g. jwks, dpop, callback")
            tbl = view
            if q:
                mask = tbl[["subject", "description", "resolution", "error_code"]] \
                    .apply(lambda s: s.str.contains(q, case=False, na=False)).any(axis=1)
                tbl = tbl[mask]
            cols = (["id", "created_at", "product", "category", "environment", "error_code", "subject",
                     "resolution_time_hrs", "escalated_to_engineer"] if officer
                    else ["created_at", "product", "category", "environment", "error_code", "subject",
                          "resolution_time_hrs"])
            st.dataframe(
                tbl[cols].sort_values("created_at", ascending=False),
                hide_index=True, width="stretch",
                column_config={"created_at": st.column_config.DateColumn("Created"),
                               "resolution_time_hrs": st.column_config.NumberColumn("Hours", format="%.1f"),
                               "escalated_to_engineer": st.column_config.CheckboxColumn("Escalated")})
            labels = {r["id"]: (f"{r['id']} · {r['subject']}" if officer else r["subject"]) for _, r in tbl.iterrows()}
            pick = st.selectbox("Open a case", ["—"] + tbl["id"].tolist(), format_func=lambda i: labels.get(i, i))
            if pick != "—":
                r = tbl[tbl["id"] == pick].iloc[0]
                with st.container(border=True):
                    st.markdown(f"**{labels[pick]}**  \n{r['product']} · {r['category']} · "
                                f"{r['environment']} · `{r['error_code']}`")
                    st.markdown(f"**Problem:** {r['description']}")
                    st.markdown(f"**Resolution:** {r['resolution']}")

        sl = slack(domain()) if officer else None
        if sl is not None and not sl.empty:
            with st.expander(f"💬 Slack threads ({len(sl)})"):
                for _, t in sl.iterrows():
                    st.markdown(f"**#{t['channel']} · {t['topic']}** — _{t['outcome']}_")

with tab_catalogue:
    cat_df = data_catalogue(domain())
    st.markdown(f"Attributes of the Myinfo **{c['openapi_schema']}** object, from the Myinfo OpenAPI spec.")
    q = st.text_input("Search attributes", key="cat_q", placeholder="e.g. address, cpf, shareholders")
    shown = cat_df
    if q:
        shown = cat_df[cat_df.apply(lambda r: q.lower() in " ".join(map(str, r.values)).lower(), axis=1)]
    st.dataframe(shown, hide_index=True, width="stretch",
                 column_config={"sub_fields": st.column_config.NumberColumn("Sub-fields"),
                                "fields": st.column_config.TextColumn("Field paths", width="large")})
    if len(cat_df) <= 15:
        st.markdown("**Sub-fields per attribute**")
        st.plotly_chart(style(px.bar(cat_df.sort_values("sub_fields"), x="sub_fields", y="attribute",
                                     orientation="h", labels={"sub_fields": "Sub-fields", "attribute": ""})),
                        width="stretch")

with tab_kb:
    s = kb_stats(domain())
    m1, m2, m3 = st.columns(3)
    m1.metric("Indexed chunks", s["total"])
    m2.metric("Official doc pages", s["doc_pages"])
    m3.metric("Historical cases", s["by_source"].get("ticket", 0) + s["by_source"].get("slack", 0))
    a, b = st.columns(2)
    with a:
        st.markdown("**Chunks by source type**")
        src = pd.DataFrame([{"source": SOURCE_TYPES.get(k, k), "chunks": v} for k, v in s["by_source"].items()])
        if not src.empty:
            st.plotly_chart(style(px.bar(src.sort_values("chunks"), x="chunks", y="source", orientation="h",
                                         labels={"chunks": "Chunks", "source": ""}), 260),
                            width="stretch")
    with b:
        st.markdown("**Chunks by product**")
        prod = pd.DataFrame([{"product": k, "chunks": v} for k, v in s["by_product"].items() if k])
        if not prod.empty:
            st.plotly_chart(style(px.bar(prod.sort_values("chunks"), x="chunks", y="product", orientation="h",
                                         labels={"chunks": "Chunks", "product": ""}), 260),
                            width="stretch")
