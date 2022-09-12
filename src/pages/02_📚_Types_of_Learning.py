import streamlit as st

st.set_page_config(
    page_title="Types of Learning",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="auto",
)

st.markdown(
    """
## Supervised Learning

Supervised learning models are models that map inputs to outputs, and attempt to
extrapolate patterns learned in past data on unseen data. Supervised learning models
can be either regression models, where we try to predict a continuous variable, like
stock prices—or classification models, where we try to predict a binary or multi-class
variable, like whether a customer will churn or not.

## Unsupervised Learning

Unsupervised learning is about discovering general patterns in data. The most popular
example is clustering or segmenting customers and users. This type of segmentation is
generalizable and can be applied broadly, such as to documents, companies, and genes.
Unsupervised learning consists of clustering models, that learn how to group similar
data points together, or association algorithms, that group different data points based
on pre-defined rules.

## Semi-Supervised Learning

Semi-supervised learning is an approach to machine learning that combines a small amount
of labeled data with a large amount of unlabeled data during training. Semi-supervised
learning falls between unsupervised learning (with no labeled training data) and supervised
learning (with only labeled training data). It is a special instance of weak supervision.
"""
)
