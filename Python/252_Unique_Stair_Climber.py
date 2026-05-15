#19-04-2026 | 19-04-2026

'''
    Problem:
        Given a number of stairs, return how many distinct ways someone can climb them
        taking either 1 or 2 steps at a time.

    Args:
        steps (int): Number of stairs.

    Return:
        int: Number of distinct ways to reach the top.
'''

def get_unique_climbs(steps):

    if steps <= 2:
        return steps

    a, b = 1, 2  # ways to reach step 1 and 2

    for _ in range(3, steps + 1):
        a, b = b, a + b

    return b