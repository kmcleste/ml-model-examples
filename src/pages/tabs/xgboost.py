from pages.tabs.utils.markdown_formatter import markdown


def xgboost():
    description = """
    Gradient Boosting algorithm that is effcient &
    flexible. Can be used for both classification and
    regression tasks.
    """

    applications = """
    1. Churn prediction
    2. Claims processing in insurance
    """

    advantages = """
    1. Provides accurate results
    2. Captures non linear relationships
    """

    disadvantages = """
    1. Hyperparameter tuning can be complex
    2. Does not perform well on sparse datasets
    """

    markdown(description, applications, advantages, disadvantages)
