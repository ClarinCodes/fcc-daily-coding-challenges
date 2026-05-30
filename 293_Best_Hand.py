# 30-05-2026 | 30-05-2026

"""
    Problem:
        Given an array of five strings representing playing cards,
        return the name of the best poker hand.

    Args:
        cards (list[str]):
            A list of 5 cards where each card is represented as
            "rank+suit" (e.g., "Ah", "7d", "Tc").

    Returns:
        str:
            The name of the best hand:
            "High Card", "Pair", "Two Pair", "Three of a Kind",
            "Straight", "Flush", "Full House",
            "Four of a Kind", "Straight Flush", or "Royal Flush".
"""

def get_best_hand(cards):
    
    rank_value = {
        '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9,
        'T': 10, 'J': 11, 'Q': 12,
        'K': 13, 'A': 14
    }

    ranks = [card[0] for card in cards]
    suits = [card[1] for card in cards]

    flush = len(set(suits)) == 1

    counts = {}
    for rank in ranks:
        counts[rank] = counts.get(rank, 0) + 1

    freqs = sorted(counts.values())

    values = sorted(rank_value[rank] for rank in ranks)

    straight = False

    if len(set(values)) == 5:
        straight = True
        for i in range(1, 5):
            if values[i] != values[i - 1] + 1:
                straight = False
                break

    if values == [2, 3, 4, 5, 14]:
        straight = True

    if flush and set(ranks) == {'A', 'K', 'Q', 'J', 'T'}:
        return "Royal Flush"
    if flush and straight:
        return "Straight Flush"
    if freqs == [1, 4]:
        return "Four of a Kind"
    if freqs == [2, 3]:
        return "Full House"
    if flush:
        return "Flush"
    if straight:
        return "Straight"
    if freqs == [1, 1, 3]:
        return "Three of a Kind"
    if freqs == [1, 2, 2]:
        return "Two Pair"
    if freqs == [1, 1, 1, 2]:
        return "Pair"

    return "High Card"


def test_cases():
    assert get_best_hand(["Ah", "Kh", "Qh", "Jh", "Th"]) == "Royal Flush"
    assert get_best_hand(["9h", "Th", "Jh", "Qh", "Kh"]) == "Straight Flush"
    assert get_best_hand(["Ah", "Ad", "Ac", "As", "7h"]) == "Four of a Kind"
    assert get_best_hand(["Ah", "Ad", "Ac", "7s", "7h"]) == "Full House"
    assert get_best_hand(["2h", "5h", "8h", "Jh", "Kh"]) == "Flush"
    assert get_best_hand(["Ah", "2d", "3c", "4s", "5h"]) == "Straight"
    assert get_best_hand(["Ah", "Ad", "Ac", "7s", "9h"]) == "Three of a Kind"
    assert get_best_hand(["Ah", "Ad", "7c", "7s", "9h"]) == "Two Pair"
    assert get_best_hand(["Ah", "Ad", "3c", "7s", "9h"]) == "Pair"
    assert get_best_hand(["Ah", "Kd", "3c", "7s", "9h"]) == "High Card"

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
