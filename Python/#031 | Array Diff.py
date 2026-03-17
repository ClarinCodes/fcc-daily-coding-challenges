#10-09-2025 | 17-03-2026

'''
    Given: two arrays
    Problem: find only the unique elements from both arrays and return those.
    Example: array_diff(["apple", "banana"], ["apple", "banana", "cherry"]) should return ["cherry"]
'''

def array_diff(arr1, arr2):
    # get elements unique to either array (symmetric difference)
    result = list(set(arr1) ^ set(arr2))
    return sorted(result)
