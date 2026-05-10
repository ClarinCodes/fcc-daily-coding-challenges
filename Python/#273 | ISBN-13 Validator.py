#10-05-2026 | 10-05-2026

'''
    Problem: 
            ISBN validator, 
                - must have length of 13, without hyphens.
                - all must be digits.
                - even index values must be multiplied by 3.

    Args: 
            s (str) - input str with or without hyphens.

    Return: 
            bool - True if all sum is divisible by 10 else False.

    is_valid_isbn_13("978-030-64061A-4") should return False.

'''

def is_valid_isbn_13(s):
    s = s.replace("-", "")

    if len(s) != 13 or not s.isdigit():
        return False

    total = 0
    for i, ch in enumerate(s):
        if i % 2 == 0:
            total += int(ch)
        else:
            total += int(ch) * 3   

    return total % 10 == 0
