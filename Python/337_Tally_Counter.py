# 13-07-2026 | 13-07-2026

"""
    Problem:
        Count the total represented by a string of tally marks.

        A tally uses:
            - "|" to represent one count.
            - "/" as the fifth mark, completing a group of five ("||||/").

    Args:
        s (str): A string containing tally marks.

    Returns:
        int: The total count represented by the tally marks.
        
"""


def get_tally_count(s):

    return sum(len(tally) for tally in s.split())

"""
def get_tally_count(s):

    total = 0
    s = s.split()
    for i in s:
        total += len(i)

    return total
"""

"""
    return s.count("|") + s.count("/")
"""
