#18-03-2026 | 18-03-2026

'''
    Given: string of int with symbols.
    Problem: seperate the int values and return. it has float values and negative values.
    Return: return the biggest value in that.
'''

def largest_number(s):
    numbers = []
    num = ""
    
    for char in s:
        if char.isdigit() or char == '-' or char == '.':
            num += char
        else:
            if num != "":
                numbers.append(float(num))
                num = ""
    
    if num != "":
        numbers.append(float(num))
    
    result = max(numbers)
    
    if result.is_integer():
        return int(result)
    return result
