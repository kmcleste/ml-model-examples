from pages.tabs.utils.markdown_formatter import markdown


def gaussian_mixture():

    topic: str = "Gaussian Mixture Model"

    description: str = """
    A probabilistic model for modeling normally
    distributed clusters within a dataset.
    """

    applications: str = """
    1. Customer segmentation
    2. Recommendation systems
    """

    advantages: str = """
    1. Computes a probability for an observation belonging to a cluster
    2. Can identify overlapping clusters
    3. More accurate results compared to K-means
    """

    disadvantages: str = """
    1. Requires complex tuning
    2. Requires setting the number of expected mixture components or clusters
    """

    markdown(topic, description, applications, advantages, disadvantages)
