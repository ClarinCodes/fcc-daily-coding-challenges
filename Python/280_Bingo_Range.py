#18-05-2026 | 18-05-2026

'''
    Problem:
        Return the number range associated with a Bingo letter.

    Args:
        letter (str): A Bingo letter ("B", "I", "N", "G", or "O").

    Return:
        list[int]: A list of numbers corresponding to the given Bingo letter range.
'''

def get_bingo_range(letter):

    bingo_ranges = {
    "B": range(1, 16),
    "I": range(16, 31),
    "N": range(31, 46),
    "G": range(46, 61),
    "O": range(61, 76),
    }

    return list(bingo_ranges[letter])
