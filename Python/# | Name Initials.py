#13-04-2026 | 13-04-2026

'''
    Args: name(string) - input full name. 
    Problem: Names to initialize are separated by a space.
                Initials should be made uppercase.
    Return: Initials seperated by dots.

'''


def get_initials(name):
    words = name.split()
    result = ""

    for word in words:
        result += word[0].upper() + "."

    return result


def test_cases():
    assert get_initials("Tommy Millwood") == "T.M."
    assert get_initials("Savanna Puddlesplash") == "S.P."
    assert get_initials("Frances Cowell Conrad") == "F.C.C."
    assert get_initials("Dragon") == "D."
    assert get_initials("Dorothy Vera Clump Haverstock Norris") == "D.V.C.H.N."

if __name__ == "__main__":
    test_cases()
    print("All test cases passed!")