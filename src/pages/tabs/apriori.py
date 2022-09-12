from pages.tabs.utils.markdown_formatter import markdown


def apriori():
    description = """
    Rule based approach that identifies the most
    frequent itemset in a given dataset where prior
    knowledge of frequent itemset properties is used.
    """

    applications = """
    1. Product placements
    2. Recommendation engines
    3. Promotion optimization
    """

    advantages = """
    1. Results are intuitive and interpretable
    2. Exhaustive approach as it finds all rules based on the confidence and support
    """

    disadvantages = """
    1. Generates many uninteresting itemsets
    2. Computationally and memory intensive
    3. Results in many overlapping item sets
    """

    markdown(description, applications, advantages, disadvantages)
