#06-04-2026 | 06-04-2026

'''
    Args: timestamp(integer) - UTC in milliseconds.
    Problem: find day of the week using millisecond.
    Return: Day(str) of the week.
'''

def get_day_of_week(timestamp):
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday"]

    if timestamp is None:
        raise ValueError("timestamp cannot be none")
    if not isinstance(timestamp, int):
        raise TypeError("timestamp must be int")

    days_since_start = timestamp // (1000 * 60 * 60 * 24)
    weekdays_index = (days_since_start + 4) % 7

    return weekdays[weekdays_index]

def test_cases():
    assert get_day_of_week(1775492249000) == "Monday"
    assert get_day_of_week(1766246400000) == "Saturday"
    assert get_day_of_week(33791256000000) == "Tuesday"
    assert get_day_of_week(1773576000000) == "Sunday"
    assert get_day_of_week(0) == "Thursday"
    print("All test cases passed!")

if __name__ == "__main__":
    test_cases()
