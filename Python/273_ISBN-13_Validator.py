#10-05-2026 | 10-05-2026

'''
    Problem:
            Determine if a given string is a valid ISBN-13 number.

    Args:
            s (str): ISBN string containing digits and hyphens.

    Return:
            bool: True if valid ISBN-13, else False.
'''

def is_valid_isbn_13(s: str) -> bool:

    for ch in s:
        if not (ch.isdigit() or ch == "-"):
            return False

    digits = [ch for ch in s if ch.isdigit()]

    if len(digits) != 13:
        return False

    total = 0
    for i, ch in enumerate(digits):
        num = int(ch)
        total += num * (1 if i % 2 == 0 else 3)

    return total % 10 == 0


def test_cases():
    assert is_valid_isbn_13("9780306406157") is True
    assert is_valid_isbn_13("97803064061570") is False
    assert is_valid_isbn_13("978-0-13-595705-9") is True
    assert is_valid_isbn_13("978-030-64061A-4") is False
    assert is_valid_isbn_13("9-7-8-0-1-3-4-7-5-7-5-9-9") is True

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()