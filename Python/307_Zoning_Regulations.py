# 13-06-2026 | 13-06-2026

"""
    Problem:
        Given a 2D grid representing a city's zoning layout, return the coordinates of all buildings that violate zoning rules.
        A building violates the rules if any of its (up, down, left, right) neighbors is a type it cannot be adjacent to.

    Args:
        grid (List[List[str]]): A 2D list where each cell contains one of:
            "i" (industrial), "A" (agricultural), "R" (residential),
            "I" (institutional), "C" (commercial), or "" (empty land).

    Return:
        List[List[int]]: A list of [row, col] coordinates of all violating cells. order does not matter.
"""

def get_zone_violations(grid):
    if not grid or not grid[0]:
        return []

    rules = {
        "i": {"R", "I"},
        "A": {"C"},
        "R": {"i", "C"},
        "I": {"i"},
        "C": {"R", "A"},
        "": set()
    }

    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    violations = set()

    for r in range(rows):
        for c in range(cols):
            current = grid[r][c]
            if current == "":
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    neighbor = grid[nr][nc]

                    if neighbor == "":
                        continue

                    if neighbor in rules[current] or current in rules[neighbor]:
                        violations.add((r, c))
                        violations.add((nr, nc))

    return [list(x) for x in violations]


def test_cases():
    assert sorted(get_zone_violations([["R", "C"], ["", "C"]])) == sorted([[0, 0], [0, 1]])
    assert sorted(get_zone_violations([["", "i"], ["", "R"], ["R", "I"]])) == sorted([[0, 1], [1, 1]])
    assert sorted(get_zone_violations([["A", "i", "C"], ["A", "", "C"], ["R", "R", "I"]])) == sorted([])
    assert sorted(get_zone_violations([
        ["R", "R", "C", "R", "R"],
        ["R", "I", "C", "", "A"],
        ["R", "R", "", "i", "A"]
    ])) == sorted([[0, 1], [0, 2], [0, 3]])

    assert sorted(get_zone_violations([
        ["R", "A", "A", "", "i", "i"],
        ["R", "I", "", "C", "i", "i"],
        ["R", "", "C", "C", "A", "A"],
        ["R", "R", "C", "I", "R", "R"]
    ])) == sorted([[2, 3], [2, 4], [3, 1], [3, 2]])

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
