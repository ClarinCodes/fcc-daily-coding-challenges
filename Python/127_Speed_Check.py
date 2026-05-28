# 15-12-2025 | 28-05-2026

"""
    Problem:
        Determine whether a driver is speeding based on their speed in MPH and the speed limit in KPH.

            - 1 mile = 1.60934 kilometers
            - Return "Not Speeding" if the speed is within the limit.
            - Return "Warning" if the speed is up to 5 KPH over the limit.
                - Return "Ticket" if the speed is more than 5 KPH over the limit.

    Args:
        speed_mph (float): The driver's speed in miles per hour.
        speed_limit_kph (float): The speed limit in kilometers per hour.

    Returns:
        str: The speeding result.
"""

def speed_check(speed_mph, speed_limit_kph):

    speed_kmph = speed_mph * 1.60934

    if speed_kmph <= speed_limit_kph:
        return "Not Speeding"

    elif speed_kmph <= speed_limit_kph + 5:
        return "Warning"

    else:
        return "Ticket"
