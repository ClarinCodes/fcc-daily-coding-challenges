#13-03-2026 | 16-03-2026

"""
    Calculate the parking fee based on entry and pickup times.

    The parking fee is calculated using the following rules:
      - Each hour costs $3.
      - Partial hours are rounded up to the next full hour.
      - If the pickup time is earlier than the park time, the parking crossed midnight
        and an additional $10 overnight fee is applied.
      - The minimum parking fee is $5.

    Args:
        park_time (str): Parking entry time in "HH:MM" 24-hour format.
        pickup_time (str): Pickup time in "HH:MM" 24-hour format.

    Returns:
        str: Total parking fee formatted as "$cost".
"""


import math
def calculate_parking_fee(park_time, pickup_time):

    pt_h, pt_m = map(int, park_time.split(":"))
    pk_h, pk_m = map(int, pickup_time.split(":"))

    park_minutes = pt_h * 60 + pt_m
    pickup_minutes = pk_h * 60 + pk_m
    overnight = False

    # if pickup time is earlier than park time, it means overnight parking
    if pickup_minutes < park_minutes:
        pickup_minutes += 24 * 60
        overnight = True

    total_minutes = pickup_minutes - park_minutes
    total_hours = math.ceil(total_minutes / 60)
    fee = total_hours * 3

    if overnight:
        fee += 10

    fee = max(fee, 5)

    return f"${fee}"
