import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def markdown(
    topic: str, description: str, applications: str, advantages: str, disadvantages: str
) -> DeltaGenerator:
    st.markdown(
        f"""
    ## {topic}

    {description}

    ### Applications

    {applications}

    ### Advantages

    {advantages}

    ### Disadvatages

    {disadvantages}
    """
    )
