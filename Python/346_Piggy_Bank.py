# 22-07-2026 | 22-07-2026 

"""
    Problem:
        Calculate the total savings in a piggy bank from a dictionary of coins.

    Args:
        coins (dict): A dictionary where keys are coin names (str) and values are counts (int).

    Returns:
        str: The total value formatted as "$D.CC".
"""

def piggy_bank(coins):

    if not coins:
        return "$0.00"

    coins_value = {
        "pennies" : 0.01,
        "nickels" : 0.05,
        "dimes" : 0.10,
        "quarters" : 0.25
    }
    total = 0

    for key, value in coins.items():
        total += coins_value[key] * value

    return f"${total:.2f}"
