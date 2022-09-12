from pages.tabs.utils.markdown_formatter import markdown


def random_forest():

    topic: str = "Random Forests"

    description: str = """
    An ensemble learning method that combines
    the output of multiple decision trees.
    """

    applications: str = """
    1. Credit score modeling
    2. Predicting housing prices
    """

    advantages: str = """
    1. Reduces overfitting
    2. Higher accuracy compared to other models
    """

    disadvantages: str = """
    1. Training complexity can be high
    2. Not very interpretable
    """

    markdown(topic, description, applications, advantages, disadvantages)
