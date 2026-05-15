#21-04-2026 | 21-04-2024

'''
    Problem: Remove even length words from the given string. 

    Args: s (str) - a sentence.

    Return: a string containing only the word with odd length.
'''

def get_odd_words(s):

    words = s.split()
    odd_words = []

    for word in words:
        if len(word)%2 != 0:
            odd_words.append(word)
    
    return " ".join(odd_words)