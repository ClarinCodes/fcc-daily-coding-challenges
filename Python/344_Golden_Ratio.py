# 20-07-2026 | 20-07-2026

"""
    Problem:
        Check if two numbers approximate the golden ratio.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        bool: True if their ratio is within 0.01 of 1.618, else False.
"""

def is_golden_ratio(a, b):

    ratio = max(a, b) / min(a, b)

    return (abs(ratio - 1.618) <= 0.01)
