# 24-05-2026 | 24-05-2026

"""
    Problem:
        Convert the given malformed roman numberals to standard roman numeral notation.
        use largest possible symbol.

            |---------------|
            |Symbol	| Value |
            |---------------|
            |"I"	  | 1     |
            |"V"	  | 5     |
            |"X"	  | 10    |
            |"L"	  | 50    |
            |"C"	  | 100   |
            |"D"	  | 500   |
            |"M"	  | 1000  |
            |---------------|

    Args:
        s (str) : Malformed roman.

    Return:
        str : Standard roman.
"""

def fix_numerals(s):

    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    roman_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = []
    total = sum(values[ch] for ch in s)

    for value, symbol in roman_map:

        count, total = divmod(total, value)
        # divmod(quotient, remainder) --> (a // b, a % b)

        result.append(symbol * count)

    return ''.join(result)


def test_cases():
    assert fix_numerals("XIIIII") == "XV"
    assert fix_numerals("IIIILX") == "LXIV"
    assert fix_numerals("XXVVVIIIII") == "XL"
    assert fix_numerals("MDCCLXXXXVIIII") == "MDCCXCIX"
    assert fix_numerals("IIIIVVVVXXXXLLLLCCDD") == "MCDLXIV"
    assert fix_numerals("ILCDMIVDIIXLCVCXDL") == "MMCMLXXXIV"

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
