#01-05-2026 | 01-05-2026

'''
    Problem: Given a list of words, group them into lists of anagrams.
             Words are anagrams if they contain the same letters in any order.

    Args: words (list of str)- A list of lowercase/uppercase strings.

    Return: a 2D list where each sublist contains words that are anagrams of each other.
'''

def group_anagrams(words):
    if not isinstance(words, list):
        raise TypeError("Input must be a list of strings")
    
    groups = {}
    
    for word in words:
        if not isinstance(word, str):
            raise TypeError("All elements must be strings")
        
        key = ''.join(sorted(word))
        
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    
    return list(groups.values())