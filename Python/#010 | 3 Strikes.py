#20-08-2025 | 29-03-2025

'''
    Given: int N.
    Problem: count how many integers from 1 to N have a square that contains the digit 3 at least once.
    Return: the count of such integers.
'''


def squares_with_three(n):
    if not isinstance(n, int):
        raise TypeError("input must be an Integer")

    count = 0
    for i in range(1, n+1):
        if '3' in str(i ** 2):
            count += 1
    return count

def test_cases():
    print(squares_with_three(1))      # 0
    print(squares_with_three(10))     # 1
    print(squares_with_three(100))    # 19
    print(squares_with_three(1000))   # 326
    print(squares_with_three(10000))  # 4531

if __name__ == "__main__":
    test_cases()
