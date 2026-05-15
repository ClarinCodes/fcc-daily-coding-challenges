#12-03-2026 | 12-03-2026

''' Given: 2D array representing a sequence of dominoes, determine whether it forms a valid chain.
    Problem: The second number of each domino must match the first number of the next domino.
             The first number of the first domino and the last number of the last domino don't need to match anything.
'''

def is_valid_domino_chain(dominoes):
    for i in range(len(dominoes)-1):
        if dominoes[i][1] != dominoes[i+1][0]:
            return False
    return True
