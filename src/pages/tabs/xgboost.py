from pages.tabs.utils.markdown_formatter import markdown


def xgboost():

    topic: str = "XGBoost"

    description: str = """
    Gradient Boosting algorithm that is effcient &
    flexible. Can be used for both classification and
    regression tasks.
    """

    applications: str = """
    1. Churn prediction
    2. Claims processing in insurance
    """

    advantages: str = """
    1. Provides accurate results
    2. Captures non linear relationships
    """

    disadvantages: str = """
    1. Hyperparameter tuning can be complex
    2. Does not perform well on sparse datasets
    """

    markdown(topic, description, applications, advantages, disadvantages)
