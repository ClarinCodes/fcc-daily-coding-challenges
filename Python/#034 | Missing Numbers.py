#13-09-2025 | 17-03-2026

'''
    Given: array of integers.
    Problem: find the missing numbers between the max and min int value.
    Return: missing numbers.
    Example: find_missing_numbers([1, 3, 5]) should return [2, 4].
'''

def find_missing_numbers(arr):
    
    biggest = max(arr)
    all_numbers = set(range(1, biggest + 1))
    found_numbers = set()
    
    for num in arr:
        if 1 <= num <= biggest:
            found_numbers.add(num)
    
    missing = all_numbers - found_numbers
    return sorted(missing)
