#07-04-2026 | 07-04-2026

'''
    Args: s(string) - input string.

    Problem: determine if it is a palindrome and extract its middle character(s) based on length parity.

    Return: the middle character (odd length), middle two characters (even length), or "none" if not a palindrome.
'''

def palindrome_locator(s):

    if s != s[::-1]:
        return "none"
    if len(s)%2 == 0:
        mid = s[(len(s)//2)-1] + s[len(s)//2]
    else:
        mid = s[len(s)//2]
        
    return mid