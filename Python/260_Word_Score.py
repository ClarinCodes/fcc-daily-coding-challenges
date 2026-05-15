#27-04-2026 | 27-04-2026

'''
    Problem: score using a standard letter-value table:

                Letter | Value
                  A	   |  1
                  B	   |  2
                 ...   |  ...
                  Z	   |  26

                Upper and lowercase letters have the same value.

    
    Args: word (string) : input string

    Return: sum of alphabets positions

'''


def get_word_score(word):

    if not isinstance(word, str):
        return "Invalid input"
    
    return sum(ord(i) - ord('a')+1 for i in word.lower() if i.isalpha())

# OR

'''
    for i in word.lower():
        if i.isalpha:
            total += ord(i) - ord('a')+1
    
    return total
'''

