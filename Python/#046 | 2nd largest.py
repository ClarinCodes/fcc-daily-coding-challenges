#25-09-2025 | 11-03-2026

''' return the second largest number in the given array '''

def second_largest(arr):
    unique = list(set(arr))  # removes duplicates
    unique.sort(reverse = True)
    return unique[1]
