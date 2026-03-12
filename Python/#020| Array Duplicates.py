#30-08-2025 | 12-03-2026 

''' Given: Array of integers. 
    Problem: Return an array of integers that appear more than once in the initial array, sorted in ascending order.
             If no values appear more than once, return an empty array.
    Example: find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]) should return [-6, 0, 2, 4, 5, 23]
'''


def find_duplicates(arr):
    seen = set()       # set() allows O(1) membership checks; using a list would be slower (O(n)) for each check
    duplicates = []    # list preserves the order of first occurrence of duplicates
    for elemt in arr:
        if elemt in seen and elemt not in duplicates:
            duplicates.append(elemt)
        else:
            seen.add(elemt)
    return sorted(duplicates)
