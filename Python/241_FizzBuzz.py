#08-04-2026 | 08-04-2026

'''
    Args: lst (list) — an array of integers and/or strings representing the sequence.
    Problem: from the given list,
                - multiples of 3 are replaced with "Fizz",
                - multiples of 5 with "Buzz",
                - multiples of both with "FizzBuzz",
            determine whether the array represents a valid FizzBuzz sequence.
    Return: True if the array is a valid FizzBuzz sequence, otherwise return False.
'''


def is_fizz_buzz(lst):
    for start in range(1, 200):
        correct = True

        for i in range(len(lst)):
            num = start + i

            if num % 3 == 0 and num % 5 == 0:
                expected = "FizzBuzz"
            elif num % 3 == 0:
                expected = "Fizz"
            elif num % 5 == 0:
                expected = "Buzz"
            else:
                expected = num

            if lst[i] != expected:
                correct = False
                break

        if correct:
            return True

    return False