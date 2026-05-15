#19-12-2025 | 19-03-2025

'''
    Given: array and target int.
    Problem: find all pairs of elements in the array whose values add up to the target.
    Return: sum of the element indices.
    Example: given [2, 3, 4, 6, 8] and 10, you will find two valid pairs:
              2 and 8 (2 + 8 = 10), whose indices are 0 and 4
              4 and 6 (4 + 6 = 10), whose indices are 2 and 3
              Add all the indices together to get a return value of 9.
'''

def pairwise(arr, target):
    total = 0
    for i in range(len(arr)):
        # Start 'j' at 'i + 1' to avoid double-counting
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                total += i + j
    return total
