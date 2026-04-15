#14-04-2026 | 14-04-2026

'''
    Problem: Find the alphabetically largest letter in a string (ignore non-letters, return first if tie)

    Args: s(String) - a string containing letters, numbers, or symbols

    Return: The letter that comes last alphabetically (first occurrence if there’s a tie)
'''

def get_last_letter(s):
    max_char = ''
    result = ''

    for c in s:
        if c.isalpha() and c.lower() > max_char:
            max_char = c.lower()
            result = c

    return result


def test_cases():
    assert get_last_letter("world") == "w"
    assert get_last_letter("Hello World") == "W"
    assert get_last_letter("The quick brown fox jumped over the lazy dog.") == "z"
    assert get_last_letter("HeLl0") == "L"
    assert get_last_letter("!#$ er@R asd fT.,> 2t0e9") == "T"

    print("All test cases passed")

if __name__ == "__main__":
    test_cases()