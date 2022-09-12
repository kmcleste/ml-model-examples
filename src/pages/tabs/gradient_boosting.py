from pages.tabs.utils.markdown_formatter import markdown


def gradient_boosting():
    description = """
    Gradient Boosting Regression employs boosting
    to make predictive models from an ensemble of
    weak predictive learners.
    """

    applications = """
    1. Predicting car emissions
    2. Pedicting ride hailing fare amount
    """

    advantages = """
    1. Better accuracy compared to other regression models
    2. It can handle multicollinearity
    3. It can handle non-linear relationships
    """

    disadvantages = """
    1. Sensitive to outliers and can therefore cause overfitting
    2. Computationally expensive and has high complexity
    """

    markdown(description, applications, advantages, disadvantages)
