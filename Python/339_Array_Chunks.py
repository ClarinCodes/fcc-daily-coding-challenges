# 15-07-2026 | 15-07-2026

"""
    Problem:
        Given an array and a chunk size, return the array split into sub-arrays of the given size.
        The last chunk may be smaller if the array cannot be divided evenly.

    Args:
        arr (list): The input array.
        size (int): The size of each chunk.

    Returns:
        list: A list of sub-arrays.
"""

def chunk_array(arr, size):

    """
    result = []

    for i in range(0, len(arr), size):
        result.append(arr[i:i + size])

    return result
    """

    return [arr[i:i + size] for i in range(0, len(arr), size)]
