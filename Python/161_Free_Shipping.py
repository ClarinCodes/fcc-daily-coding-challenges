#18-01-2026 | 18-04-2026

'''
    Problem: find whether the buyer is eligible for free shipping or not.

    Args: cart (list) --> name of the products,
          minimum (int) --> minimum amount for eligibility.

    Return: boolean value.

'''


def gets_free_shipping(cart, minimum):
    total = 0
    array = [
    ["shirt", 34.25],
    ["jeans", 48.50],
    ["shoes", 75.00],
    ["hat", 19.95],
    ["socks", 15.00],
    ["jacket", 109.95]
]
    for i in range(len(cart)):
        for j in range(len(array)):
            if cart[i] == array[j][0]:
                total += array[j][1]
                break
    
    if total >= minimum:
        return True
    else:
        return False
