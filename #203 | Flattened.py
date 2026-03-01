#01-03-2026 | 01-03-2026

''' check wherter the given array is 1D or 2D and return True or False '''

def is_flat(arr):
    for i in arr:
        if isinstance(i,list):
            return False
    return True
