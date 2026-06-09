# 09-06-2026 | 09-06-2026

"""
    Problem:
        Pair people within the same group.

    Args:
        data (list[dict]): People with "name" and "group" keys.

    Returns:
        list[str]: Roommate pairs joined with " and "; unpaired people remain alone.
"""

def get_roommates(data):
    groups = {}
    result = []

    for person in data:
        group = person["group"]
        if group not in groups:
            groups[group] = []
        groups[group].append(person["name"])

    for names in groups.values():
        for i in range(0, len(names), 2):
            if i + 1 < len(names):
                result.append(names[i] + " and " + names[i + 1])
            else:
                result.append(names[i])

    return result
