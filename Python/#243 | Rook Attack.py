#10-04-2026 | 10-04-2026

'''
    Args: rook1/2 (string) - position of rook with the combination of char and int.
    Problem: they can attack each other if they are in same row or column.
    Return: True if they can attack otherwise False.
'''


def rook_attack(rook1, rook2):
    return rook1[0] == rook2[0] or rook1[1] == rook2[1]

def test_cases():
    assert rook_attack("A1", "A8") == True
    assert rook_attack("B4", "F4") == True
    assert rook_attack("E3", "D4") == False
    assert rook_attack("H7", "F6") == False
    print("All test cases passed")

if __name__ == "__main__":
    test_cases()