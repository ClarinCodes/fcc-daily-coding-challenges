# 01-09-2026 | 02-09-2026

"""
    Problem:
        Generate a Tribonacci sequence of the given length.
        The next number in the sequence is the sum of the previous three numbers.

    Args:
        start_sequence (list[int]): The first three integers of the sequence.
        length (int): The required length of the sequence.

    Returns:
        list[int]: The Tribonacci sequence containing `length` integers.
"""


def tribonacci_sequence(start_sequence, length):
    if length <= 3:
        return start_sequence[:length]

    result = start_sequence[:]

    for i in range(length - 3):
        result.append(result[i] + result[i + 1] + result[i + 2])

    return result
