#15-03-2026 | 15-03-2026

'''
Given: An array of chess pieces you still have on the board.
Problem: Calculate the total value of pieces your opponent captured.
Return: Total value of captured pieces, or "Checkmate" if the king is captured.
'''
#the values are given on this problem site


def get_captured_value(pieces_on_board):
    start = {
        "P": 8,
        "R": 2,
        "N": 2,
        "B": 2,
        "Q": 1,
        "K": 1
    }

    values = {
        "P": 1,
        "R": 5,
        "N": 3,
        "B": 3,
        "Q": 9,
        "K": 0
    }

    for p in pieces_on_board:
        start[p] -= 1

    if start["K"] == 1:
        return "Checkmate"

    total = 0
    for p in start:
        total += start[p] * values[p]

    return total
