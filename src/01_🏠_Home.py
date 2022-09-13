import streamlit as st

st.set_page_config(
    page_title="Home", page_icon="🏠", layout="centered", initial_sidebar_state="auto"
)

st.markdown("# ML Playground")

# TODO: Add welcome message and description of website purpose

st.markdown(
    """
### Table of Contents

1. Home - you are here ⭐️
2. Types of Learning
3. Model Evaluation Metrics

**Supervised Learning**

4. Linear Models
   1. Linear Regression
   2. Logistic Regression
   3. Ridge Regression
   4. Lasso Regression
5. Tree-Based Models
   1. Decision Tree
   2. Random Forest
   3. Gradient Boosting Regression
   4. XGBoost
   5. LightGBM Regression

**Unsupervised Learning**

6. Clustering
   1. K-Means
   2. Hierarchical Clustering
   3. Gaussian Mixture Models
7. Association
   1. Apriori Algorithm

---

### Sources

DataCamp: [Machine Learning Cheat Sheet](https://www.datacamp.com/cheat-sheet/machine-learning-cheat-sheet)
"""
)
