# 23-07-2026 | 23-07-2026

def play_game(p1, p2):
    score1 = 0
    score2 = 0

    for a, b in zip(p1, p2):
        if a == "C" and b == "C":
            score1 += 3
            score2 += 3
        elif a == "D" and b == "D":
            score1 += 1
            score2 += 1
        elif a == "D" and b == "C":
            score1 += 5
        else:
            score2 += 5

    return [score1, score2]
