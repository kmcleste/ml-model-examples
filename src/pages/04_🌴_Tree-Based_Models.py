import streamlit as st

from pages.tabs.decision_tree import decision_tree
from pages.tabs.random_forest import random_forest
from pages.tabs.gradient_boosting import gradient_boosting
from pages.tabs.xgboost import xgboost
from pages.tabs.lightgbm import lightgbm

st.set_page_config(
    page_title="Page 3",
    page_icon="🌴",
    layout="centered",
    initial_sidebar_state="auto",
)

(_decision_tree, _random_forest, _gradient_boosting, _xgboost, _lightgbm) = st.tabs(
    [
        "Decision Tree",
        "Random Forest",
        "Gradient Boost Regression",
        "XGBoost",
        "LightGBM Regressor",
    ]
)

with _decision_tree:
    decision_tree()

with _random_forest:
    random_forest()

with _gradient_boosting:
    gradient_boosting()

with _xgboost:
    xgboost()

with _lightgbm:
    lightgbm()
