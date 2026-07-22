# 22-12-2025 | 22-07-2026

"""
    Problem:
        Determine how many items can be bought with the available funds.

    Args:
        funds (list[str]): [amount, currency_code].
        items (list[list[str]]): List of item prices in the same format.

    Returns:
        str:
            "Buy them all!" if every item can be afforded; otherwise,
            "Buy the first X items.", where X is the number of consecutive items that can be purchased.
"""


def buy_items(funds, items):
    rates = {
        "USD": 1.00,
        "EUR": 1.10,
        "GBP": 1.25,
        "JPY": 0.007,
        "CAD": 0.75
    }

    money = float(funds[0]) * rates[funds[1]]

    for index, (price, currency) in enumerate(items):
        cost = float(price) * rates[currency]

        if money < cost:
            return f"Buy the first {index} items."

        money -= cost

    return "Buy them all!"
