# 27-07-2026 | 27-07-2026

def is_pronic(n):

    if n == 0:
        return True

    # Calculate integer square root.
    k = int(n ** 0.5)
    return k * (k + 1) == n
