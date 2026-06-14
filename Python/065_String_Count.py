# 14-10-2025 | 14-06-2026

"""
    Problem:
        Determine how many times the second string appears in the first string.

    Args:
        text (str) : First string.
        parameter (str) : Second string.

    Return:
        int : Count of 'parameter' appeared in 'text'.
"""

def count(text, parameter):
    result = 0

    for i in range(len(text) - len(parameter) + 1):
        if text[i:i+len(parameter)] == parameter:
            result += 1

    return result


def test_cases():
    assert count('abcdefg', 'def') == 1
    assert count('hello', 'world') == 0
    assert count('mississippi', 'iss') == 2
    assert count('she sells seashells by the seashore', 'sh') == 3
    assert count('101010101010101010101', '101') == 10

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
