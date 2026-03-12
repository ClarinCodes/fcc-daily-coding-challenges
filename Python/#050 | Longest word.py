#29-09-2025 | 12-03-2026

''' Given: sentence, return longest word. 
           Ignore periods (.) when determining word length. if more the one word occur with same len then return the first word.
    Example: get_longest_word("This sentence has multiple long words.") should return "sentence".
'''

def get_longest_word(sentence):
    words = sentence.replace(".", "").split()
    return max(words, key=len)
