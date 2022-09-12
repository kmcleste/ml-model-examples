from pages.tabs.utils.markdown_formatter import markdown


def lasso_regression():
    description = """
    Part of the regression family — it penalizes
    features that have low predictive outcomes by
    shrinking their coeOcients to zero. Can be used
    for classification or regression.
    """

    applications = """
    1. Predicting housing prices
    2. Predicting clinical outcomes based on health data
    """

    advantages = """
    1. Less prone to overfitting
    2. Can handle high-dimensional data
    3. No need for feature selection
    """

    disadvantages = """
    1. Can lead to poor interpretability as it can keep highly correlated variables
    """

    markdown(description, applications, advantages, disadvantages)
