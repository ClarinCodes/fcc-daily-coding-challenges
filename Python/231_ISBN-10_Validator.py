#29-03-2026 | 29-03-2026

'''
   Given: 's' string of isbn.
   Problem: 1. remove the hyphens '-'.
            2. the first 9 char must be digits. 
            3. the 'x' char has the value = 10 and it must be at the end.
            4. multiply each value by its position and add them.
    Return: True if the sum is divisible by 11, else False.

'''



def is_valid_isbn10(s):
    digits = []
    
    for i, char in enumerate(s):
        if char == '-':
            continue
        if char.isdigit():
            digits.append(int(char))
        elif char == 'X':
            # 'X' is only valid as the last character
            if i == len(s) - 1:
                digits.append(10)
            else:
                return False
        else:
            return False

    # Must have exactly 10 digits after removing hyphens
    if len(digits) != 10:
        return False

    # First 9 must be digits (not 10)
    if 10 in digits[:-1]:
        return False

    values = 0
    for i in range(len(digits)):
        values += (i + 1) * digits[i]
    
    if values % 11 == 0:
        return True
    
    return False

def test_cases():
    print(is_valid_isbn10("0-306-40615-2"))    # True
    print(is_valid_isbn10("0-306-40615-1"))    # False
    print(is_valid_isbn10("0-8044-2957-X"))    # True
    print(is_valid_isbn10("X-306-40615-2"))    # False
    print(is_valid_isbn10("0-6822-2589-4"))    # True

if __name__ == "__main__":
    test_cases()
