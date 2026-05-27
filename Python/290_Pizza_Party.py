# 27-05-2026 | 27-05-2026

"""
    Problem:
        Find the number of pizzas to order based on workers hours worked. 
            - Each 3 hours worked earns 1 slice.
            - Each worker receives a minimum of two slices.
            - Round up both the slice count and pizza count.

    Args:
        hours_worked (lst[int]) : A list of integers representing the hours worked by each worker.

    Return:
        int : Total number of pizzas to order.

"""

import math

def get_pizzas_to_order(hours_worked):

    slices = 0

    for i in hours_worked:
        needed = math.ceil(i/3)

        if needed < 2:
            needed = 2
            
        slices += needed

    return math.ceil(slices/8)
