# 16-07-2026 | 16-07-2026

"""
    Problem:
        Convert a sentence into Pig Latin. Words beginning with a vowel
        have "way" added to the end. Words beginning with a consonant
        move the leading consonant(s) to the end and then add "ay".

    Args:
        s (str): A sentence containing one or more words.

    Returns:
        str: The sentence converted to Pig Latin.
"""

def pig_latin(s):
    vowels = "aeiou"
    words = s.split()
    result = []

    for word in words:
        if word[0].lower() in vowels:
            if word[0].isupper():
                result.append(word + "way")
            else:
                result.append(word + "way")

        else:
            upper = word[0].isupper()
            word = word.lower()

            i = 0
            while i < len(word) and word[i] not in vowels:
                i += 1

            pig = word[i:] + word[:i] + "ay"

            if upper:
                pig = pig.capitalize()

            result.append(pig)


    return " ".join(result)


def test_cases():
    assert pig_latin("apple") == "appleway"
    assert pig_latin("hello") == "ellohay"
    assert pig_latin("string") == "ingstray"
    assert pig_latin("apple banana") == "appleway ananabay"

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
