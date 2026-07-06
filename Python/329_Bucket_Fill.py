# 05-07-2026 | 06-07-2026

"""
    Problem:
        Replace the value at the starting position and all horizontally or
        vertically connected cells with the same value using the new value.

    Args:
        grid (list): A 2D list representing the grid.
        pos (list): The starting position as [row, col].
        new_value (str): The value to replace the connected cells with.

    Return:
        list: The updated grid after performing the bucket fill.
"""

def bucket_fill(grid, pos, new_value):
    rows = len(grid)
    cols = len(grid[0])

    r, c = pos
    old_value = grid[r][c]

    if old_value == new_value:
        return grid

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != old_value:
            return

        grid[r][c] = new_value

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(r, c)
    return grid

def test_cases():

    assert bucket_fill(
        [["T", "T", "R", "T"],
         ["R", "T", "R", "T"],
         ["R", "T", "R", "T"],
         ["T", "T", "T", "T"]],
        [0, 3],
        "Y"
    ) == [["Y", "Y", "R", "Y"],
          ["R", "Y", "R", "Y"],
          ["R", "Y", "R", "Y"],
          ["Y", "Y", "Y", "Y"]]

    assert bucket_fill(
        [["G", "B", "G", "B"],
         ["R", "B", "B", "G"],
         ["B", "G", "B", "R"],
         ["B", "G", "G", "B"]],
        [2, 2],
        "G"
    ) == [["G", "G", "G", "B"],
          ["R", "G", "G", "G"],
          ["B", "G", "G", "R"],
          ["B", "G", "G", "B"]]

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
