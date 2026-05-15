#08-01-2026 | 07-03-2026

''' problem: check the given array and return whether it is ascending, descending or not sorted '''

def is_sorted(arr):
    if arr == sorted(arr):
        return "Ascending"
    elif arr == sorted(arr, reverse = True):
        return "Descending"
    else:
        return "Not sorted"
