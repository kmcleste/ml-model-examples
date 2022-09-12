from pages.tabs.utils.markdown_formatter import markdown


def gaussian_mixture():
    description = """
    A probabilistic model for modeling normally
    distributed clusters within a dataset.
    """

    applications = """
    1. Customer segmentation
    2. Recommendation systems
    """

    advantages = """
    1. Computes a probability for an observation belonging to a cluster
    2. Can identify overlapping clusters
    3. More accurate results compared to K-means
    """

    disadvantages = """
    1. Requires complex tuning
    2. Requires setting the number of expected mixture components or clusters
    """

    markdown(description, applications, advantages, disadvantages)
