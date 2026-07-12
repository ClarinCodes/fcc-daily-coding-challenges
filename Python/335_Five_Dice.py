# 11-07-2026 | 12-07-2026

"""
    Problem:
        Given an array of five dice with values from 1 to 6, determine
        and return the best possible poker-style hand according to the
        following rankings (lowest to highest):

        - "no pair"
        - "pair"
        - "two pair"
        - "three of a kind"
        - "small straight"
        - "large straight"
        - "full house"
        - "four of a kind"
        - "five of a kind"

    Args:
        dice (list[int]): A list of exactly five integers, where each
        integer is between 1 and 6 inclusive.

    Return:
        str: The highest-ranking hand that can be formed from the five dice.
"""

def five_dice(dice):
    freq = [0] * 7

    for d in dice:
        freq[d] += 1

    counts = sorted([x for x in freq if x > 0], reverse=True)
    s = set(dice)

    if counts == [5]:
        return "five of a kind"

    if counts == [4, 1]:
        return "four of a kind"

    if counts == [3, 2]:
        return "full house"

    if s == {1, 2, 3, 4, 5} or s == {2, 3, 4, 5, 6}:
        return "large straight"

    if ({1, 2, 3, 4} <= s or
        {2, 3, 4, 5} <= s or
        {3, 4, 5, 6} <= s):
        return "small straight"

    if counts == [3, 1, 1]:
        return "three of a kind"

    if counts == [2, 2, 1]:
        return "two pair"

    if counts == [2, 1, 1, 1]:
        return "pair"

    return "no pair"
