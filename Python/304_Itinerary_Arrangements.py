# 10-06-2026 | 10-06-2026

"""
    Problem:
        Count the number of valid itinerary arrangements.

    Args:
        stops (list[str]): Optional stops (length >= 2).

    Returns:
        int: Number of valid itineraries.
"""

from math import factorial

def get_itinerary_count(stops):

    n = len(stops)
    return factorial(n) * (2 * n - 3)
