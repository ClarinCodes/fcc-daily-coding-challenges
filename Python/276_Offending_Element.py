#13-05-2026 | 13-05-2026

'''
    Problem:
            Find the index of the element that breaks the sorted order.

    Args:
            arr (list[int]): A nearly sorted list of integers containing exactly one out-of-order element.

    Returns:
            int: The index of the offending element.
'''

def find_offender(arr):
    n = len(arr)

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return i if i == 0 or arr[i - 1] <= arr[i + 1] else i + 1
