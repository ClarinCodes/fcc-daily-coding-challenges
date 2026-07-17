# 17-07-2026 | 17-07-2026

# Calculte the number of days until the next birthday.

from datetime import date, datetime

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_until_birthday(today, birthday):
    month, day = map(int, birthday.split("/"))
    today = datetime.strptime(today, "%Y-%m-%d").date()

    year = today.year

    while True:
        # Skip invalid Feb 29 in non-leap years
        if month == 2 and day == 29 and not is_leap(year):
            year += 1
            continue

        bday = date(year, month, day)

        if bday <= today:   # today counts as next year's birthday
            year += 1
            continue

        return (bday - today).days
