# 18-06-2026 | 18-06-2026

"""
    Problem:
        Calculate the total cost of movies in a cart and apply a discount based on the subscription tier.

        Pricing:
                        "rent"     "buy"
            "HD"        $3.99      $12.99
            "4K"        $5.99      $19.99

        Subscription discounts:
            "none"    -> 0% off
            "basic"   -> 10% off
            "premium" -> 25% off

    Args:
        cart (list[dict[str, str]]) : A list of movies, each containing:
            - "format": "HD" or "4K"
            - "type": "rent" or "buy"

        subscription (str) : Subscription tier ("none", "basic", or "premium")

    Returns:
        str : Total cost formatted as "$D.CC"
"""


def get_streaming_bill(cart, subscription):

    prices = {
        ("HD", "rent"): 3.99,
        ("HD", "buy"): 12.99,
        ("4K", "rent"): 5.99,
        ("4K", "buy"): 19.99
    }

    discount = {
        "none": 0,
        "basic": 0.10,
        "premium": 0.25
    }

    total = 0

    for item in cart:
        price = prices[(item["format"], item["type"])]
        price -= price * discount[subscription]
        total += price

    return f'${total:.2f}'


def test_cases():
    assert get_streaming_bill(
        [{"format": "HD", "type": "rent"}],
        "none"
    ) == "$3.99"

    assert get_streaming_bill(
        [{"format": "HD", "type": "rent"}, {"format": "HD", "type": "buy"}],
        "premium"
    ) == "$12.73"

    assert get_streaming_bill(
        [{"format": "HD", "type": "rent"}, {"format": "HD", "type": "rent"}, {"format": "HD", "type": "buy"}],
        "basic"
    ) == "$18.87"

    assert get_streaming_bill(
        [{"format": "4K", "type": "buy"}, {"format": "4K", "type": "buy"}],
        "premium"
    ) == "$29.98"

    assert get_streaming_bill(
        [
            {"format": "HD", "type": "rent"},
            {"format": "4K", "type": "rent"},
            {"format": "HD", "type": "buy"},
            {"format": "4K", "type": "buy"}
        ],
        "none"
    ) == "$42.96"

    assert get_streaming_bill(
        [
            {"format": "HD", "type": "rent"},
            {"format": "4K", "type": "rent"},
            {"format": "HD", "type": "buy"},
            {"format": "4K", "type": "buy"},
            {"format": "HD", "type": "buy"}
        ],
        "basic"
    ) == "$50.36"

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
