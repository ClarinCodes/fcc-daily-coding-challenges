#03-03-2026 | 03-03-2026

'''
Given: Two integers a and b where the smaller number is not guaranteed to be the first argument.
Problem: Count how many perfect cubes exist between a and b (inclusive).
Return: An integer representing the total number of perfect cubes in the given range.
Example: count_perfect_cubes(3, 30) → 2, count_perfect_cubes(-64, 64) → 9.
'''

def count_perfect_cubes(a, b):
    if a > b:
        a, b = b, a
    count = 0
    for i in range(-10000, 10001):
        cube = i * i * i
        if a <= cube <= b:
            count += 1

    return count
