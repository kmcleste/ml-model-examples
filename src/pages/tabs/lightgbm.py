from pages.tabs.utils.markdown_formatter import markdown


def lightgbm():

    topic: str = "LightGBM Regressor"

    description: str = """
    A gradient boosting framework that is designed
    to be more effcient than other implementations.
    """

    applications: str = """
    1. Predicting flight time for airlines
    2. Predicting cholesterol levels based on health data
    """

    advantages: str = """
    1. Can handle large amounts of data
    2. Computational efficient & fast training speed
    3. Low memory usage
    """

    disadvantages: str = """
    1. Can overfit due to leaf-wise splitting and high sensitivity
    2. Hyperparameter tuning can be complex
    """

    markdown(topic, description, applications, advantages, disadvantages)
