# 04-09-2025 | 05-09-2026

def repeat_vowels(s):

    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    count = 1

    for char in s:
        if char.lower() in vowels:
            result.append(char + char.lower() * (count - 1))
            count += 1
        else:
            result.append(char)

    return ''.join(result)
