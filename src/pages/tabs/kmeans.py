from pages.tabs.utils.markdown_formatter import markdown


def kmeans():
    description = """
    K-Means is the most widely used clustering
    approach—it determines K clusters based on
    euclidean distances.
    """

    applications = """
    1. Customer segmentation
    2. Recommendation systems
    """

    advantages = """
    1. Scales to large datasets
    2. Simple to implement and interpret
    3. Results in tight clusters
    """

    disadvantages = """
    1. Requires the expected number of clusters from the beginning
    2. Has troubles with varying cluster sizes and densities
    """

    markdown(description, applications, advantages, disadvantages)
