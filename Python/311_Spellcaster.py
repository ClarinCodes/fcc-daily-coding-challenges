# 17-06-2026 | 17-06-2026

"""
    Problem:
        Calculate the total power of a sequence of spells. Each spell belongs
        to a category and has a base score. Consecutive spells from different
        categories increase the multiplier, while spells from the same category
        reset the multiplier to 1.

    Args:
        spells (str): A string where each character represents a spell:
            f, l -> Destruction (score 3)
            i, w -> Control (score 2)
            h, s -> Restoration (score 1)

    Returns:
        int: The total power score after applying category-based multipliers.
"""

def cast(spells):

    spell_data = {
        'f': ('Destruction', 3),
        'l': ('Destruction', 3),
        'i': ('Control', 2),
        'w': ('Control', 2),
        'h': ('Restoration', 1),
        's': ('Restoration', 1)
    }

    first_category, first_score = spell_data[spells[0]]

    multiplier = 1
    total = first_score * multiplier
    prev_cat = first_category

    for char in spells[1:]:

        category, score = spell_data[char]

        if category != prev_cat:
            multiplier += 1
        else:
            multiplier = 1

        total += score * multiplier
        prev_cat = category

    return total
