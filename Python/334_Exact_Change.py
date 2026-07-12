# 10-07-2026 | 12-07-2026

"""
    Problem:
        Given an integer amount in cents, return the number of distinct
        ways to make exact change using pennies (1 cent), nickels (5 cents),
        dimes (10 cents), and quarters (25 cents).

    Args:
        amount (int): The amount of money in cents.

    Return:
        int: The number of distinct ways to make exact change.
"""

def exact_change(amount):
    coins = [1, 5, 10, 25]
    ways = [0] * (amount + 1)
    ways[0] = 1

    for coin in coins:
        for i in range(coin, amt + 1):
            ways[i] += ways[i - coin]

    return ways[amt]
