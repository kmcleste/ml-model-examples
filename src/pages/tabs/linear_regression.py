from pages.tabs.utils.markdown_formatter import markdown


def linear_regression():
    description = """
    A simple algorithm that models a linear
    relationship between inputs and a continuous
    numerical output variable."""

    applications = """
    1. Stock price prediction
    2. Predicting housing price
    3. Predicting customer lifetime value"""

    advantages = """
    1. Explainable method
    2. Interpretable results by its output coefficients
    3. Faster to train than other machine learning models"""

    disadvantages = """
    1. Assumes linearity between inputs and output
    2. Sensitive to outliers
    3. Can underfit with small, high-dimensional data"""

    markdown(description, applications, advantages, disadvantages)
