#15-04-2026 | 15-04-2026

'''
    Problem: Sort the integers in ascending order, Then swap all values whose index is a multiple of 3
             with the value before it.

    Args: arr(list) -  a list with n integer elements. 

    Return: the array after applying sorting and index-based swapping.
'''


def sort_and_swap(arr):

    if not isinstance(arr, list):
        return "Error: Input must be a list"

    if len(arr) < 4:
        return arr  # nothing to swap

    arr.sort()
    for i in range(3, len(arr), 3):
        arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr



def test_cases():
    assert sort_and_swap([1, 2, 3, 4, 5, 6]) == [1, 2, 4, 3, 5, 6]
    assert sort_and_swap([10, 20, 30, 40, 50, 60, 70, 80, 90]) == [10, 20, 40, 30, 50, 70, 60, 80, 90]
    assert sort_and_swap([1, 2, 3]) == [1, 2, 3]
    assert sort_and_swap([1, 2, 3, 4]) == [1, 2, 4, 3]

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()