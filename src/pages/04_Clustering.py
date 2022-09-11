import streamlit as st

from pages.tabs import kmeans, hierarchical, gaussian_mixture

st.set_page_config(
    page_title="Page 4",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="auto",
)
