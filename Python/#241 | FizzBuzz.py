#08-04-2026 | 08-04-2026

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