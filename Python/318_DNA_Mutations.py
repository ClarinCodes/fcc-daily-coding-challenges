# 24-06-2026 | 24-06-2026

"""
    Problem:
        Given two DNA strands of equal length, return the indices where they differ.
        DNA strands contain only: 'A', 'T', 'C', 'G'.

    Args:
        strand1 (str): First DNA strand.
        strand2 (str): Second DNA strand.

    Returns:
        list[int]:  Indices where the characters differ, or an empty list if no mutations are found.
"""


def detect_mutations(strand1, strand2):

    return [i for i in range(len(strand1)) if strand1[i] != strand2[i]]
