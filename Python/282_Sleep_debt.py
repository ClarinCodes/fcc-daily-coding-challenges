# 19-05-2026 | 19-05-2026

"""
Problem:
    Find the hours of sleep you need tonight to eliminate your sleep debt.

Args:
    hours_slept (list[int]): Last 6 days of sleep hours.
    target_hours (int): Target sleep hours per day.

Returns:
    int: Sleep debt. Returns 0 if no debt.

Time Complexit: O(n)
Space Complexity: O(1)

"""


def sleep_debt(hours_slept, target_hours):

    total_sleep = target_hours * 7 - sum(hours_slept)

    return max(0, total_sleep)


def test_cases():
    assert sleep_debt([6, 6, 6, 6, 6, 6], 8) == 20
    assert sleep_debt([6, 7, 8, 4, 8, 6], 7) == 10
    assert sleep_debt([10, 10, 9, 10, 9, 11], 9) == 4
    assert sleep_debt([8, 7, 6, 7, 6, 8], 6) == 0
    assert sleep_debt([8, 9, 10, 9, 10, 7], 7) == 0

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
