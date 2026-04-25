#02-01-2026 | 25-04-2026


'''
    Problem:
        Find the nth Fibonacci number where:
        F(0) = 0, F(1) = 1
        F(n) = F(n-1) + F(n-2) for n >= 2

    Args:
        n (int): index of Fibonacci number to compute (0-based)

    Return:
        int: the nth Fibonacci number
'''

def nth_fibonacci(n: int) -> int:

    if n == 1:
        return 0
    if n == 2:
        return 1

    a, b = 0, 1

    for _ in range(3, n + 1): # _ == any variable
        a, b = b, a + b

    return b