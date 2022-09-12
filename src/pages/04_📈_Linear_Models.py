import streamlit as st

from pages.tabs.linear_regression import linear_regression
from pages.tabs.logistic_regression import logistic_regression
from pages.tabs.lasso_regression import lasso_regression
from pages.tabs.ridge_regression import ridge_regression

st.set_page_config(
    page_title="Linear Models",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="auto",
)

(
    _linear_regression,
    _logistic_reggresion,
    _ridge_regression,
    _lasso_regression,
) = st.tabs(
    ["Linear Regression", "Logistic Regression", "Ridge Regression", "Lasso Regression"]
)

with _linear_regression:
    linear_regression()

with _logistic_reggresion:
    logistic_regression()

with _ridge_regression:
    ridge_regression()

with _lasso_regression:
    lasso_regression()
