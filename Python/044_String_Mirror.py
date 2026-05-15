#23-09-2025 | 11-03-2026

''' Given: two strings are given, determine if the second string is a mirror of the first.
           Ignore all non-alphabetical characters.
'''


def is_mirror(str1, str2):
    clean_str = ""

    for char in str2:
        if char.isalpha() or char.isspace():
            clean_str += char
        elif char == "-":
            clean_str += " "

    if clean_str == str1[::-1]:
        return True
        
    return False
