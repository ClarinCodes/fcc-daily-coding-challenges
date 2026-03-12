#14-08-2025 | 12-03-2026

''' Given: string.
    Problem:  remove all spaces from the string, insert two spaces between every character, convert all letters to uppercase.
    Example: space_jam("Hello World?!") should return "H  E  L  L  O  W  O  R  L  D  ?  !"
'''

def space_jam(s):
    
    s = s.replace(" ", "").upper()
    result = "  ".join(s)
    
    return result
