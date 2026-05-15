#24-09-2026 | 24-03-2026

'''
    Given: int (squared number).
    Problem: determine whether it is a perfect square.
    Return: boolean value, True if the square has a whole value, otherwise False.
    Example: 9 is a perfect square because you can multiply 3 by itself to get it.
'''

import math
def is_perfect_square(n):

    if n < 0:
        return False

    root = int(math.sqrt(n))
    if n == root*root:
        return True
    return False

def main():
    print(is_perfect_square(9))   # True
    print(is_perfect_square(49))  # True
    print(is_perfect_square(1))   # True
    print(is_perfect_square(2))   # False

if __name__ == "__main__":
    main()
