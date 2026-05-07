#12-08-2025 | 07-05-2026

def is_valid_number(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    allowed = set(digits[:base])

    return all(ch in allowed for ch in n.upper())
