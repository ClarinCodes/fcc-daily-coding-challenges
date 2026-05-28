# 28-05-2026 | 28-05-2026

"""
    Problem:
        Count the number of fizz and buzz appearances within the given range.
            - Numbers divisible by 3 count as a fizz.
            - Numbers divisible by 5 count as a buzz.
            - Numbers divisible by both 3 and 5 count as both a fizz and a buzz.

    Args:
        start (int): The starting number of the range.
        end (int): The ending number of the range.

    Returns:
        dict: A dictionary containing the counts of fizz and buzz.
"""

def fizz_buzz_count(start, end):

    fizz_buzz = {
        "fizz" : 0,
        "buzz" : 0
    }

    for i in range(start, end + 1):

        if i%3 == 0:
            fizz_buzz["fizz"] += 1

        if i%5 == 0:
            fizz_buzz["buzz"] += 1

    return fizz_buzz


def test_cases():
    assert fizz_buzz_count(1, 11) == {"fizz": 3, "buzz": 2}
    assert fizz_buzz_count(14, 41) == {"fizz": 9, "buzz": 6}
    assert fizz_buzz_count(24, 100) == {"fizz": 26, "buzz": 16}
    assert fizz_buzz_count(-635, -14) == {"fizz": 207, "buzz": 125}
    assert fizz_buzz_count(-5432, 6789) == {"fizz": 4074, "buzz": 2444}

    print("All test cases passed!")

if __name__ == "__main__":
    test_cases()
