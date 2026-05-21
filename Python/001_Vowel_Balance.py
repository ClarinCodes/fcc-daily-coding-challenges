# 11-08-2025 | 21-05-2026

"""
    Problem:
        Check if the number of vowels in the first half of a string equals the number in the second half.
        If the string length is odd, ignore the middle character.

    Args:
        s (str): Input string.

    Return:
        bool: True if both halves have equal vowel counts, else False.
"""

def is_balanced(s):

    vowels = set("aeiouAEIOU")
    mid = len(s)// 2

    left = 0
    right = 0

    for i, ch in enumerate(s):
        if len(s) % 2 == 1 and i == mid:
            continue

        if ch in vowels:
            if i < mid:
                left += 1
            else:
                right += 1

    return left == right


def test_cases():
    assert is_balanced("racecar") == True
    assert is_balanced("Lorem Ipsum") == True
    assert is_balanced("Kitty Ipsum") == False
    assert is_balanced("string") == False
    assert is_balanced("abcdefghijklmnopqrstuvwxyz") == False 

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
