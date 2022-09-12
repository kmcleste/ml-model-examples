from pages.tabs.utils.markdown_formatter import markdown


def random_forest():
    description = """
    An ensemble learning method that combines
    the output of multiple decision trees.
    """

    applications = """
    1. Credit score modeling
    2. Predicting housing prices
    """

    advantages = """
    1. Reduces overfitting
    2. Higher accuracy compared to other models
    """

    disadvantages = """
    1. Training complexity can be high
    2. Not very interpretable
    """

    markdown(description, applications, advantages, disadvantages)
