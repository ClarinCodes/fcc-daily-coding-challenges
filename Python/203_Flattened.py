#01-03-2026 | 01-03-2026

''' check wherter the given array has a list or not '''

def is_flat(arr):
    for i in arr:
        if isinstance(i,list):
            return False
    return True
