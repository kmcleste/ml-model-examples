from pages.tabs.utils.markdown_formatter import markdown


def lightgbm():
    description = """
    A gradient boosting framework that is designed
    to be more effcient than other implementations.
    """

    applications = """
    1. Predicting flight time for airlines
    2. Predicting cholesterol levels based on health data
    """

    advantages = """
    1. Can handle large amounts of data
    2. Computational efficient & fast training speed
    3. Low memory usage
    """

    disadvantages = """
    1. Can overfit due to leaf-wise splitting and high sensitivity
    2. Hyperparameter tuning can be complex
    """

    markdown(description, applications, advantages, disadvantages)
