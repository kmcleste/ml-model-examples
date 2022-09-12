from pages.tabs.utils.markdown_formatter import markdown


def decision_tree():

    topic: str = "Decision Tree"

    description: str = """
    Decision Tree models make decision rules on
    the features to produce predictions. It can be
    used for classification or regression.
    """

    applications: str = """
    1. Customer churn predictioI
    2. Credit score modeling
    3. Disease prediction
    """

    advantages: str = """
    1. Explainable and interpretable
    2. Can handle missing values
    """

    disadvantages: str = """
    1. Prone to overfitting
    2. Sensitive to outliers
    """

    markdown(topic, description, applications, advantages, disadvantages)
