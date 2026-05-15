#22-04-2026 | 22-04-2026

'''
    Problem:
            Calculate a score from a list of items using base values, streak bonuses, and periodic multipliers.
            Rules:
                - Normal items have fixed base values.
                - Consecutive same items gain a streak bonus (+1, +2, +3, ...).
                - "rare" items are given as ["rare", value]:
                    - Use given value directly
                    - No streak bonus
                    - Reset streak
                - Every 5th item gets a multiplier:
                    - 5th → ×2, 10th → ×3, etc.
                    - Apply multiplier after adding bonuses.

    Args:
         items (list) - List of item names or ["rare", value] entries.

Return:
        int - Total computed score.
'''



def get_cleanup_score(items):

    base_values = {
        "bottle": 10,
        "can": 6,
        "bag": 8,
        "tire": 35,
        "straw": 4,
        "cardboard": 3,
        "newspaper": 3,
        "shoe": 12,
        "electronics": 25,
        "battery": 18,
        "mattress": 38
    }

    total = 0
    streak_count = 0
    prev_type = None

    for i, item in enumerate(items, start=1):

        # 1. Determine type + base value
        if isinstance(item, list) and item[0] == "rare":
            item_type = "rare"
            value = item[1]
        else:
            item_type = item
            value = base_values[item_type]

        # 2. Streak bonus
        if item_type == "rare":
            streak_count = 0
            bonus = 0
        else:
            if item_type == prev_type:
                streak_count += 1
            else:
                streak_count = 1

            bonus = streak_count - 1

        score = value + bonus

        # 3. Multiplier every 5th item
        if i % 5 == 0:
            multiplier = (i // 5) + 1
        else:
            multiplier = 1

        score *= multiplier

        # 4. Add to total
        total += score

        prev_type = item_type

    return total

def test_cases():
        assert get_cleanup_score(["bottle", "straw", "shoe", "battery"]) == 44
        assert get_cleanup_score(["electronics", "straw", "newspaper", "bottle", "bag"]) == 58
        assert get_cleanup_score(["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"]) == 79
        assert get_cleanup_score(["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]]) == 358
        assert get_cleanup_score(["bottle", "can", "can", "shoe", "shoe", ["rare", 56],
                                  "bottle", "bottle", "can", "can", "electronics", "bottle",
                                  ["rare", 48], "bottle", "can", "can", "can", "can", "can", "can", "can"]) == 383
        
if __name__ == "__main__":
    test_cases()