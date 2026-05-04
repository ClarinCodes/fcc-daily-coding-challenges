#04-05-2026 | 04-05-2026

'''

    Problem:
            Convert parsecs into time or distance based on parity (odd → time, even → distance).
    
    Args:
            parsecs (int): number of parsecs.
    
    Return:
            int: parsecs * 2 if odd, parsecs * 3 if even.

'''

def convert_parsecs(parsecs):

    return parsecs * 3 if parsecs %2 == 0 else parsecs * 2