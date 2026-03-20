#27-10-2025 | 18-03-2026 

'''
    Given: N with int value
    Problem: create a string with all of the integers from 1 up to, and including, the given number, in numerical order.
    Return: created string.
    Example:  sequence(5) should return "12345".
'''


def sequence(n):
    string = ""

    for i in range(1, n+1):
        string += str(i)
      # OR
    string = ''.join(str(i) for i in range(1, n+1)) #best case in both O(n)
    
    return string

      # OR

    return "".join(f"{i}" for i in range(1, n+1))
