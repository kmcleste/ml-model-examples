from pages.tabs.utils.markdown_formatter import markdown


def logistic_regression():

    topic: str = "Logistic Regression"

    description: str = """
    A simple algorithm that models a linear
    relationship between inputs and a categorical
    output (1 or 0).
    """

    applications: str = """
    1. Credit risk score prediction
    2. Customer churn prediction
    """

    advantages: str = """
    1. Interpretable and explainable
    2. Less prone to overfitting when using regularization
    3. Applicable for multi-class predictions
    """

    disadvantages: str = """
    1. Assumes linearity between inputs and outputs
    2. Can overfit with small, highldimensional data
    """

    markdown(topic, description, applications, advantages, disadvantages)
