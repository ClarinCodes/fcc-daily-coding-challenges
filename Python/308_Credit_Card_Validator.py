# 14-06-2026 | 14-06-2026

"""
    Problem:
        Validate a credit card number (uses the Luhn algorithm).
            Rules:
                - Starting from the second-to-last digit, moving left, double every other digit.
                - If doubling a digit results in a number greater than 9, subtract 9.
                - Sum all digits (both modified and untouched).
                - If the total sum is divisible by 10, the number is valid.

    Args:
        number (str): A string of digits representing the credit card number.

    Return:
        bool: True if valid, False otherwise.
"""

def is_valid_card(number):
    number = number[::-1]
    total = 0

    for pos, digit in enumerate(number):
        n = int(digit)

        if pos % 2 != 0:
            doubled = n * 2
            total += doubled - 9 if doubled > 9 else doubled
        else:
            total += n

    return total % 10 == 0


def test_cases():
    assert is_valid_card("4532015112830366") == True
    assert is_valid_card("5425233430109903") == True
    assert is_valid_card("371449635398431") == True
    assert is_valid_card("6011111111111117") == True
    assert is_valid_card("4532015112830367") == False
    assert is_valid_card("1234567890123456") == False
    assert is_valid_card("4532015112830368") == False

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
