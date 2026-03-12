#22-09-2025 | 12-03-2026

''' Given: string
    Problem: count only the char(upper and lower) and int. return which count is high.
    Example: digits_or_letters("abc123!@#DEF") should return "letters".
             digits_or_letters("H3110 W0R1D") should return "digits".
             digits_or_letters("P455W0RD") should return "tie".
'''


def digits_or_letters(s):
  
    digits = 0
    letters = 0 
    for char in s:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1

  # OR 
  ''' digits = sum(1 for c in s if c.isdigit())   # count all digits, 1 is the incremental value.
    letters = sum(1 for c in s if c.isalpha())  # count all letters '''
            
    if digits > letters:
        return "digits"
    elif digits < letters:
        return "letters"
    else:
        return "tie"
