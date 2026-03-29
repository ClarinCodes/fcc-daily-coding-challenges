#18-08-2025 | 29-03-2026 

'''
    Given: int N (0 <= n <= 20).
    Problem: Factorial = Product of all the numbers between 1 and give number.
    Return: 1 only if the N is 0, otherwise return the factorial value.
'''


def factorial(n):
    if n < 0 or n > 20:
        return "input must be between 0 and 20"

    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def test_cases():
    print(factorial(0))   # 1
    print(factorial(5))   # 120
    print(factorial(20))  # 2432902008176640000

if __name__ == "__main__":
    test_cases()
