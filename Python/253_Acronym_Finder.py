#20-04-2026 | 20-04-2026


'''
    Args: acronym (str): Input acronym string.

    Problem: The program returns the full form of the given acronym from a predefined mapping.

    Returns: str - Expanded full form of the acronym.
'''

def find_org(acronym):
    names = {
        "NASA": "National Avocado Storage Authority",
        "CIA": "Cats Infiltration Agency",
        "FBI": "Fluffy Beanbag Inspectors",
        "DOJ": "Department Of Jelly",
        "WHO": "Wild Honey Organization",
        "EPA": "Eating Pancakes Administration",
    }

    try:
        return names[acronym]
    except KeyError:
        return "Error: Acronym not found"


def test_cases():
    assert find_org("NASA") == "National Avocado Storage Authority"
    assert find_org("CIA") == "Cats Infiltration Agency"
    assert find_org("XYZ") == "Error: Acronym not found"

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()