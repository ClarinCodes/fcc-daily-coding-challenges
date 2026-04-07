#07-04-2026 | 07-04-2026


def palindrome_locator(s):

    if s != s[::-1]:
        return "none"
    if len(s)%2 == 0:
        mid = s[(len(s)//2)-1] + s[len(s)//2]
    else:
        mid = s[len(s)//2]
        
    return mid