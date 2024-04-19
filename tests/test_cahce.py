import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.check_cache import query_cache


def test_query_cache():
    """
    Test the query_cache function.
    Ensure that the top cosine similarity score is greater than the threshold.
    """
    query = "Who is the director of the Duke AI Master of Engineering program?"
    threshold = 0.9
    top_similarity_scores = query_cache(query, threshold)
    assert top_similarity_scores[0][1] > threshold


if __name__ == "__main__":
    test_query_cache()

