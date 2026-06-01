# 17-11-2025 | 31-05-2026 

def is_match(fingerprint_a, fingerprint_b):
    if len(fingerprint_a) != len(fingerprint_b):
        return False

    wrong = 0
    n = len(fingerprint_a)

    for i in range(n):
        if fingerprint_a[i] != fingerprint_b[i]:
            wrong += 1

    return wrong <= (n / 10)
