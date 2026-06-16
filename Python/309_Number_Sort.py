# 15-06-2026 | 16-06-2026

"""
    Problem:
        Sort the numbers in a string.

    Args:
        s (str) : Numbers seperated by comma.

    Return:
        lst : sorted numbers

    Example:
        sort_numbers("3,1,2") should return [1, 2, 3].
"""

def sort_numbers(s):

    return sorted([int(x) for x in s.split(',')])
