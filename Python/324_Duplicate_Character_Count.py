# 30-06-2026 | 30-06-2026

"""
    Problem:
        Count characters in `str2` that exist in `str1`.

    Args:
        str1 (str): String to search.
        str2 (str): Characters to check.

    Return:
        int: The number of matching characters.
"""

def duplicate_character_count(str1, str2):

    return sum(char in str1 for char in str2)
