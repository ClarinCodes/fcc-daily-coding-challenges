#30-10-2025 | 21-03-2025

'''
    Given: N.
    Problem: return the Nth prime number.
    Example: nth_prime(5) should return 11.
'''

def nth_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num
