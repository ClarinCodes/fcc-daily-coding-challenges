# 26-12-2025 | 07-07-2026

# given 6, return 12 because the divisors of 6 are 1, 2, 3, and 6, and the sum of those is 12.

def sum_divisors(n):

    return sum(num for num in range(1,n+1) if n%num == 0)
