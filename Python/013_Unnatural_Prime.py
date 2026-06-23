# 23-08-2025 | 23-06-2026

"""
    Problem:
        Determine if a number is a prime number or a negative prime number.
        A prime number is a positive integer greater than 1 that has no divisors
        other than 1 and itself. A negative prime number is the negative form of
        a positive prime number. 0, 1, and -1 are not considered prime.

    Args:
        n (int): The integer to check.

    Return:
        bool: True if n is a prime or negative prime number, otherwise False.
"""

def is_unnatural_prime(n):
    if n in (0, 1, -1):
        return False

    num = abs(n)

    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True
