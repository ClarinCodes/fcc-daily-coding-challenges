# 18-07-2026 | 03-08-2026

def get_odds(dice, target):
    total = 6 ** dice
    success = 0

    def count(rolled, current_sum):
        nonlocal success

        if rolled == dice:
            if current_sum == target:
                success += 1
            return

        for i in range(1, 7):
            count(rolled + 1, current_sum + i)

    count(0, 0)

    odds = round(total / success)
    return f"1 in {odds}"
