# 02-07-2026 | 02-07-2026

"""
    Problem:
        Determine the maximum profit that can be made by buying and selling a stock over the given period.

    Args:
        prices (list): Daily stock prices.
        budget (int): Available budget.

    Returns:
        str: Maximum profit formatted to two decimal places.
"""


def get_max_profit(prices, budget):
    max_profit = 0

    for i in range(len(prices)):
        buy_price = prices[i]
        shares = int(budget // buy_price)

        for j in range(i + 1, len(prices)):
            sell_price = prices[j]
            profit = shares * (sell_price - buy_price)

            if profit > max_profit:
                max_profit = profit

    return f"{max_profit:.2f}"

def test_cases():
    assert get_max_profit([5, 6], 50) == "10.00"
    assert get_max_profit([8, 2, 5, 10], 20) == "80.00"
    assert get_max_profit([4, 5, 3, 6], 20) == "18.00"
    assert get_max_profit([54.40, 51.22, 53.99, 50.28, 53.01, 52.84], 200) == "8.31"
    assert get_max_profit([15.38, 15.01, 14.99, 14.62, 14.28], 80) == "0.00"
    assert get_max_profit([121.45, 126.82, 122.91, 124.65, 128.83, 128.83, 127.33], 1230.25) == "73.80"

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
