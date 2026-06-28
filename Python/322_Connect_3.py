# 28-06-2026 | 28-06-2026

"""
    Problem:
        Given a matrix of strings representing pieces on a game grid, determine if any player has same type three in a row.
        it can be horizontally, vertically, or diagonally.

    Args:
        matrix (list[list]): Each element will be "R", "Y", or "" (empty string).

    Return:
        list: An array with the winner and the three coordinates of the winner.
        format: ["R", [0,2], [1,3], [2,4]]. An empty array if there is no winner.
"""


def connect_three(board):
    rows = len(board)
    cols = len(board[0])

    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (1, 1),   # diagonal down-right
        (1, -1)   # diagonal down-left
    ]

    for r in range(rows):
        for c in range(cols):

            if board[r][c] == "":
                continue

            for dr, dc in directions:

                r1 = r + dr
                c1 = c + dc

                r2 = r + 2 * dr
                c2 = c + 2 * dc

                # Check if all positions are inside the board
                if not (0 <= r2 < rows and 0 <= c2 < cols):
                    continue

                if (board[r][c] == board[r1][c1] ==
                        board[r2][c2]):

                    return [
                        board[r][c],
                        [r, c],
                        [r1, c1],
                        [r2, c2]
                    ]

    return []

def test_cases():
    assert connect_three([
        ["", "", "", ""],
        ["", "", "", ""],
        ["", "Y", "", ""],
        ["Y", "R", "R", "R"]
    ]) == ["R", [3, 1], [3, 2], [3, 3]]

    assert connect_three([
        ["", "", "", ""],
        ["", "Y", "Y", ""],
        ["", "Y", "R", "R"],
        ["", "Y", "R", "R"]
    ]) == ["Y", [1, 1], [2, 1], [3, 1]]

    assert connect_three([
        ["", "", "Y", "R"],
        ["", "Y", "R", "Y"],
        ["", "R", "Y", "R"],
        ["", "R", "Y", "R"]
    ]) == ["R", [0, 3], [1, 2], [2, 1]]

    assert connect_three([
        ["", "Y", "", ""],
        ["", "Y", "Y", ""],
        ["", "R", "R", "Y"],
        ["R", "R", "Y", "R"]
    ]) == ["Y", [0, 1], [1, 2], [2, 3]]

    assert connect_three([
        ["Y", "R", "R", "Y"],
        ["R", "Y", "Y", "R"],
        ["Y", "R", "R", "Y"],
        ["R", "Y", "Y", "R"]
    ]) == []

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
