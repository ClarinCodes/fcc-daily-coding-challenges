#27-01-2026 | 07-03-2026

''' problem: find date using given millisecond and return whether the date is odd or even '''


def odd_or_even_day(timestamp):
    
    from datetime import datetime
    date = datetime.utcfromtimestamp(timestamp / 1000).day

    if (date % 2) == 0:
        return "even"
    else:
        return "odd"
