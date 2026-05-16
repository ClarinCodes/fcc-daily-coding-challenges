#12-05-2026 | 12-05-2026

'''
    Problem:
            Count the char frequency in given string.

    Args:
            s (str) - input string

    Return:
            dict - where {"char" : count}

    get_frequency("test") should return {"t": 2, "e": 1, "s": 1}.
'''

def get_frequency(s):
    freq = {}

    for ch in s:

        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    return freq
