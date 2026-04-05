#05-05-2026 | 05-05-2026

'''
    Args: n (int): A positive number.
    Problem: Check each rotation of n to see if it is divisible by its number of digits.
    Return: int or str: The index of the first rotation that works, or "none" if none do.
'''

def get_rotation(n):
    n = str(n)

    for i in range(len(n)-1):
        if int(n) % len(n) == 0:
            return i
        n = n[1:] + n[0]
    return "none"


def test_cases():
    assert get_rotation(123) == 0
    assert get_rotation(1234) == 2
    assert get_rotation(13) == "none"
    assert get_rotation(84138789345) == 6
    assert get_rotation(25) == "none"
    print("All test cases passed!")

if __name__ == "__main__":
    test_cases()
