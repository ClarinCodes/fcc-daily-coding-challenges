# 26-07-2026 | 26-07-2026

def letter_distance(str1, str2):
    total = 0

    for a, b in zip(str1, str2):
        diff = abs(ord(a) - ord(b))
        total += min(diff, 26 - diff)

    return total
