# 04-07-2026 | 06-07-2026

"""
    Problem:
        Given a 4-digit number, return the number of times Kaprekar's
        routine must be applied to reach 6174.

    Args:
        num (int): A 4-digit integer.

    Return:
        int: The number of steps required to reach 6174.
"""

def kaprekar(num):
    count = 0

    while num != 6174:
        digits = str(num).zfill(4)  # zfill() is a string method that adds leading zeros

        large = int("".join(sorted(digits, reverse=True)))
        small = int("".join(sorted(digits)))

        num = large - small
        count += 1

    return count


def test_cases():
    assert kaprekar(1234) == 3
    assert kaprekar(2025) == 6
    assert kaprekar(7173) == 4
    assert kaprekar(3164) == 7
    assert kaprekar(8082) == 2

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
