# 06-01-2026 | 21-07-2026

"""
    Problem:
        Converts all vowels to uppercase and all consonants to lowercase.
        Non-alphabetic characters remain unchanged.

    Args:
        s (str): The input string.

    Returns:
        str: The transformed string with adjusted casing.

    vowel_case("coding is fun") should return "cOdIng Is fUn".
"""

def vowel_case(s):

    vowels = set("aeiou")
    result = []

    for char in s:
        if char.isalpha():
            if char.lower() in vowels:
                result.append(char.upper())

            else:
                result.append(char.lower())

        else:
            result.append(char)

    return "".join(result)
