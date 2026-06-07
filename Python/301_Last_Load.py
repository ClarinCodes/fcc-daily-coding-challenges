# 07-06-2026 | 07-06-2026

"""
    Problem:
        Given remaining scoops of detergent and past daily usage, estimate how many full days the detergent will last using average daily usage.

    Args:
        scoops (int): Remaining detergent scoops.
        usage (List[int]): Array of scoops used per day.

    Return:
        int: Number of full days the detergent will last.
"""

def last_load_date(scoops, usage):

    return scoops//(sum(usage)/len(usage))
