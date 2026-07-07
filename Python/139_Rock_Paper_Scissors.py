# 27-12-2025 | 07-07-2026

def rock_paper_scissors(player1, player2):

    beats = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }

    if player1 == player2:
        return "Tie"

    if beats[player1] == player2:
        return "Player 1 wins"

    return "Player 2 wins"
