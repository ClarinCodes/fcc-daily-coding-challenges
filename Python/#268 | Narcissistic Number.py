#06-05-2026 | 06-05-2026

'''
    Problem:
        Determine whether a number is a narcissistic number.

    Args:
        n (int): A positive integer.

    Return:
        bool: True if n is narcissistic, otherwise False.
'''

def is_narcissistic(n):

    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)

# Test cases
print(is_narcissistic(153))   # True
print(is_narcissistic(154))   # False
