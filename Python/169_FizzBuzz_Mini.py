#26-01-2026 | 26-04-2026


def fizz_buzz_mini(n):

    if n%3 ==0 and n%5 == 0:
        return "FizzBuzz"
    elif n%3 == 0:
        return "Fizz"
    elif n%5 == 0:
        return "Buzz"
    else:
        return str(n)