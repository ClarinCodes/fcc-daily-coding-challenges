# 17-10-2025 | 14-06-2026

"""
    Problem:
        Mask all numbers except last four digits.
        Mask numbers by using '*'.

    Args:
        card (str) : Card numbers (seperated by single space or hyphen).

    Return:
        str : Masked card numbers.
"""

def mask(card):
    result = []
    digits_seen = sum(c.isdigit() for c in card)
    hide = digits_seen - 4

    count = 0
    for c in card:
        if c.isdigit() and count < hide:
            result.append('*')
            count += 1
        elif c.isdigit():
            result.append(c)
            count += 1
        else:
            result.append(c)

    return ''.join(result)

def test_cases():
    assert mask("4012-8888-8888-1881") == "****-****-****-1881"
    assert mask("5105 1051 0510 5100") == "**** **** **** 5100"
    assert mask("6011 1111 1111 1117") == "**** **** **** 1117"
    assert mask("2223-0000-4845-0010") == "****-****-****-0010"

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
