import streamlit as st

from pages.tabs import (
    decision_tree,
    random_forest,
    gradient_boosting,
    xgboost,
    lightgbm,
)

st.set_page_config(
    page_title="Page 3",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="auto",
)
