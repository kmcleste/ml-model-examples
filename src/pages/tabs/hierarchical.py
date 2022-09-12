from pages.tabs.utils.markdown_formatter import markdown


def hierarchical():

    topic: str = "Hierarchical Clustering"

    description: str = """
    A bottom-up approach where each data
    point is treated as its own cluster — and then
    the closest two clusters are merged together
    iteratively.
    """

    applications: str = """
    1. Fraud detection
    2. Document clustering based on similarity
    """

    advantages: str = """
    1. There is no need to specify the number of clusters
    2. The resulting dendrogram is informative
    """

    disadvantages: str = """
    1. Doesn't always result in the best clustering
    2. Not suitable for large datasets due to high complexity
    """

    markdown(topic, description, applications, advantages, disadvantages)
