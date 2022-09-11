import streamlit as st

from pages.tabs import (
    linear_regression,
    logistic_regression,
    ridge_regression,
    lasso_regression,
)

st.set_page_config(
    page_title="Page 2",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="auto",
)
