import streamlit as st

from pages.tabs.kmeans import kmeans
from pages.tabs.hierarchical import hierarchical
from pages.tabs.gaussian_mixture import gaussian_mixture

st.set_page_config(
    page_title="Page 4",
    page_icon="📏",
    layout="centered",
    initial_sidebar_state="auto",
)

_kmeans, _hierarchical, _gaussian_mixture = st.tabs(
    ["K-Means Clustering", "Hierarchical Clustering", "Gaussian Mixture Models"]
)

with _kmeans:
    kmeans()

with _hierarchical:
    hierarchical()

with _gaussian_mixture:
    gaussian_mixture()
