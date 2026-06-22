# 22-08-2025 | 22-06-2026

def decode(s, shift):
    res = []

    for c in s:
        if 'a' <= c <= 'z':
            x = ord(c) - ord('a')
            x = (x - shift) % 26
            res.append(chr(x + ord('a')))
        elif 'A' <= c <= 'Z':
            x = ord(c) - ord('A')
            x = (x - shift) % 26
            res.append(chr(x + ord('A')))
        else:
            res.append(c)

    return ''.join(res)
