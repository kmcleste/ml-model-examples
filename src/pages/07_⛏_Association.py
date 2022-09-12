import streamlit as st

from pages.tabs.apriori import apriori

st.set_page_config(
    page_title="Association",
    page_icon="⛏",
    layout="centered",
    initial_sidebar_state="auto",
)

apriori()
