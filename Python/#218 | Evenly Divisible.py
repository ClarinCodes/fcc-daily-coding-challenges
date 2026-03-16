#16-03-2026 | 16-03-2026

'''
    Given: A and B with int values.
    Problem: divide A with B and check whether the value is float or int
    Return: True if the value is int, else False
'''

def is_evenly_divisible(a, b):
    c = a/b    # Forces float division (int/int → float)
    if c.is_integer() == True:  # Redundant `== True`
        return True
    return False
 # OR
    #return a%b == 0 
