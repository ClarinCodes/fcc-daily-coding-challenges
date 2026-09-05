# 03-09-2025 | 05-09-2026

"""
    True if the sentence(str) letters are in letters(str) else False.
    ignore letter casing and non-alphabetical characters.
"""

def is_pangram(sentence, letters):
    sentence = set(sentence.lower())
    letters = set(letters.lower())

    sentence = {letter for letter in sentence if letter.isalpha()}

    return sentence == letters
