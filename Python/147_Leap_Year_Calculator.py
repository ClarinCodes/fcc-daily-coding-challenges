#04-01-2026 | 21-03-2026

'''
    Given: year.
    Problem: find leap year or not,
                -The year is evenly divisible by 4, and
                -The year is not evenly divisible by 100, unless
                -The year is evenly divisible by 400.
    Return: true or false.
'''

def is_leap_year(year):
    
    if (year % 4 == 0 and year % 100 != 0) or year%400 == 0:
        return True
    return False
