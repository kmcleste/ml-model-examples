from pages.tabs.utils.markdown_formatter import markdown


def logistic_regression():
    description = """
    A simple algorithm that models a linear
    relationship between inputs and a categorical
    output (1 or 0).
    """

    applications = """
    1. Credit risk score predictioI
    2. Customer churn prediction
    """

    advantages = """
    1. Interpretable and explainable
    2. Less prone to overfitting when using regularization
    3. Applicable for multi-class predictions
    """

    disadvantages = """
    1. Assumes linearity between inputs and outputs
    2. Can overfit with small, highldimensional data
    """

    markdown(description, applications, advantages, disadvantages)
