import streamlit as st

st.set_page_config(
    page_title="Home", page_icon="🏠", layout="centered", initial_sidebar_state="auto"
)

st.markdown("# ML Playground")

# TODO: Add welcome tag and description of website purpose
st.markdown("## Welcome! 👋")

st.markdown(
    """
### Table of Contents

1. Supervised Learning
   1. Linear Models
      1. Linear Regression
      2. Logistic Regression
      3. Ridge Regression
      4. Lasso Regression
   2. Tree-Based Models
      1. Decision Tree
      2. Random Forest
      3. Gradient Boosting Regression
      4. XGBoost
      5. LightGBM Regression
2. Unsupervised Learning
   1. Clustering
      1. K-Means
      2. Hierarchical Clustering
      3. Gaussian Mixture Models
   2. Association
      1. Apriori Algorithm

"""
)
