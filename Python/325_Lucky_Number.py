# 01-07-2026 | 01-07-2026

"""
    Problem:
        Given a person's first and last name as a single string, compute a lucky number
        based on vowel and consonant counts in each name.

        - Form one value using the smaller vowel count, smaller consonant count, and shorter name length. - Form another value using the larger vowel count,
        larger consonant count, and longer name length.
        -The lucky number is the difference between the larger and smaller values.
        - If the result is 0, return 13.
    
    Args:
        name (str): A string containing exactly two names separated by a space.

    Return:
        int: The calculated lucky number.
"""

def get_lucky_number(name):
    first, last = name.split()

    def counts(s):
        vowels = sum(c.lower() in "aeiou" for c in s)
        consonants = sum(c.isalpha() and c.lower() not in "aeiou" for c in s)
        return vowels, consonants

    v1, c1 = counts(first)
    v2, c2 = counts(last)

    small = min(v1, v2) * min(c1, c2) * min(len(first), len(last))
    large = max(v1, v2) * max(c1, c2) * max(len(first), len(last))

    lucky = large - small
    return 13 if lucky == 0 else lucky


def test_cases():
    assert get_lucky_number("John Doe") == 21
    assert get_lucky_number("Olivia Lewis") == 52
    assert get_lucky_number("James Wilson") == 18
    assert get_lucky_number("Elizabeth Hernandez") == 81
    assert get_lucky_number("Mike Walker") == 32
    assert get_lucky_number("Chloe Perez") == 13

    print("All tests passed!")


if __name__ == "__main__":
    test_cases()
