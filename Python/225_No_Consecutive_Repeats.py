#23-03-2026 | 23-03-2026

'''
    Given: A string 's'
    Problem: determine whether it contains any consecutive repeating characters.
    Return: Boolean values, True if the string has no repeating character otherwise False.
'''

def has_no_repeats(s):
    for char in range(len(s) - 1):
        if s[char] == s[char + 1]:
            return False
    return True

# test cases
def main():
    print(has_no_repeats("hello world")) #False
    print(has_no_repeats("hi world"))    #True


if __name__ == "__main__":
    main()
