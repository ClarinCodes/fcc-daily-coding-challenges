#28-03-2026 | 28-03-2026

'''
    Given: int N.
    Problem: In Pascal's Triangle: - Each row begins and ends with 1
                                   - Each interior value is the sum of the two values directly above it from the previous row.​
    Return: Nth row of Pascal's triangle as an array.
'''

def pascal_row(n):
    # Handle invalid input
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    
    if n < 0:
        raise ValueError("n must be non-negative")
    
    # Handle edge case
    if n == 0:
        return [1]
    
    row = [1]
    for k in range(1, n):
        next_val = row[-1] * (n - k) // k
        row.append(next_val)
    
    return row

def test_cases():
    print(pascal_row(0))   # [1]
    print(pascal_row(1))   # [1]
    print(pascal_row(3))   # [1, 2, 1]
    print(pascal_row(5))   # [1, 4, 6, 4, 1]
    print(pascal_row(10))  # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    print(pascal_row(15))  # [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1]


if __name__ == "__main__":
    test_cases()
