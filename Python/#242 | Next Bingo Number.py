#09-04-2026 | 09-04-2026

'''
    Args: s (string) — a valid bingo number in the format Letter+Number (e.g., "B10").
    Problem: find the next sequential bingo number, wrapping to the next letter when the range ends and cycling back to "B1" after "O75".
    Return: the next bingo number in sequence as a string.
'''

def get_next_bingo_number(s):
    letter = s[0]
    num = int(s[1:])

    ranges = {
        "B": (1, 15),
        "I": (16, 30),
        "N": (31, 45),
        "G": (46, 60),
        "O": (61, 75)
    }

    order = ["B", "I", "N", "G", "O"]

    start, end = ranges[letter]

    # normal increment case
    if num < end:
        return f"{letter}{num + 1}"

    # move to next letter
    next_index = (order.index(letter) + 1) % len(order)
    next_letter = order[next_index]

    next_start = ranges[next_letter][0]

    return f"{next_letter}{next_start}"

def test_cases():
    assert get_next_bingo_number("B10") == "B11"
    assert get_next_bingo_number("N33") == "N34"
    assert get_next_bingo_number("I30") == "N31"
    assert get_next_bingo_number("G60") == "O61"
    assert get_next_bingo_number("O75") == "B1"
    print("All test cases passed")

if __name__ == "__main__":
    test_cases()