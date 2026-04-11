#11-04-2026 | 11-04-2026


"""
    Problem:Given positions of a rook and a bishop on a chessboard (A1 to H8), determine which piece can attack the other.

    Args: rook (str): position of rook (e.g., "A1")
          bishop (str): position of bishop (e.g., "C3")

    Returns: str: "rook" if rook attacks bishop,
                  "bishop" if bishop attacks rook,
                  "neither" if no attack possible,
                  "invalid" if input is outside A-H / 1-8
    """


def rook_bishop_attack(rook, bishop):

    if not ('A' <= rook[0] <= 'H' and '1' <= rook[1] <= '8'):
        return "invalid"
    if not ('A' <= bishop[0] <= 'H' and '1' <= bishop[1] <= '8'):
        return "invalid"

    r_row, r_col = int(rook[1]) - 1, ord(rook[0]) - ord('A')
    b_row, b_col = int(bishop[1]) - 1, ord(bishop[0]) - ord('A')

    if rook[0] == bishop[0] or rook[1] == bishop[1]:
        return "rook"

    if abs(r_row - b_row) == abs(r_col - b_col):
        return "bishop"

    return "neither"


def test_cases():
    assert rook_bishop_attack("A1", "A8") == "rook"
    assert rook_bishop_attack("A1", "H8") == "bishop"
    assert rook_bishop_attack("A1", "B3") == "neither"
    assert rook_bishop_attack("A1", "Z9") == "invalid"
    assert rook_bishop_attack("H1", "H8") == "rook"
    assert rook_bishop_attack("C1", "F4") == "bishop"
    print("all test cases passed")

if __name__ == "__main__":
    test_cases()