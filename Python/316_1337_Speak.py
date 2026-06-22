# 22-06-2026 | 22-06-2026

# Replacing characters in given string.


def make_leet(s):

    char_sub = {
        "a" : 4,
        "e" : 3,
        "g" : 9,
        "i" : 1,
        "l" : 1,
        "o" : 0,
        "s" : 5,
        "t" : 7
    }
    new = ""

    for char in s:

        if char in char_sub:
            new += str(char_sub[char])
        else:
            new += char

    return new

"""
 OR

    return "".join(char_sub.get(char, char) for char in s)

    """
