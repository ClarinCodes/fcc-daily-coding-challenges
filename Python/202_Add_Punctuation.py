#28-02-2026 | 16-05-2026

'''
    Problem:
        Insert a period (".") before each space that precedes an uppercase letter,  and at the end of the string.

    Args:
        text (str): Input string without periods.

    Returns:
        str: String with periods inserted correctly.
'''

def add_punctuation(text):
    result = []

    for i in range(len(text)):
        if text[i] == ' ' and i + 1 < len(text) and text[i + 1].isupper():
            result.append('.')
        result.append(text[i])

    return ''.join(result) + '.'
