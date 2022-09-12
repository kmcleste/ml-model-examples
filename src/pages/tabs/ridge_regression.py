from pages.tabs.utils.markdown_formatter import markdown


def ridge_regression():

    topic: str = "Ridge Regression"

    description: str = """
    Part of the regression family — it penalizes
    features that have low predictive outcomes by
    shrinking their coefficients closer to zero. Can
    be used for classification or regression.
    """

    applications: str = """
    1. Predictive maintenance for automobile8
    2. Sales revenue prediction
    """

    advantages: str = """
    1. Less prone to overfitting
    2. Best suited where data suffers from multicollinearity
    3. Explainable & interpretable
    """

    disadvantages: str = """
    1. All the predictors are kept in the final model
    2. Doesn't perform feature selection
    """

    markdown(topic, description, applications, advantages, disadvantages)
