import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def markdown(
    description: str, applications: str, advantages: str, disadvantages: str
) -> DeltaGenerator:
    st.markdown(
        f"""
    ## Description

    {description}

    ## Applications

    {applications}

    ## Advantages

    {advantages}

    ## Disadvatages

    {disadvantages}
    """
    )
