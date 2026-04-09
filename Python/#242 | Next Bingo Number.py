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
