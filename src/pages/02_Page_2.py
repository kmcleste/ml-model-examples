import streamlit as st
from pages.tabs.tab import tab1 as _tab1
from pages.tabs.tab import tab2 as _tab2

st.set_page_config(
    page_title="Page 2",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="auto",
)

st.markdown("# Page 2")

tab1, tab2 = st.tabs(["tab1", "tab2"])

with tab1:
    _tab1()

with tab2:
    _tab2()
