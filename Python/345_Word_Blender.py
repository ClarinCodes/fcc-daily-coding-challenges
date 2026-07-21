# 21-07-2026  | 21-07-2026

"""
    Problem:
        Combine the first half of the first word and second half of the second word.

    Args:
        word1 (str): First word.
        word2 (str): Second word.

    Return:
        str: New word created by combining words.
"""

def blend_words(word1, word2):

    first = word1[: len(word1)//2]
    second = word2[ len(word2)//2 :]

    return first + second
