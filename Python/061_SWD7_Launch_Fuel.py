# 10-10-2025 | 10-06-2026

"""
    Problem:
        Given a payload mass, compute the fuel needed to lift the
        payload and the fuel itself.

    Args:
        payload (float): Payload mass in kg.

    Returns:
        float: Fuel required, rounded to 1 decimal place.
"""

def launch_fuel(payload):

    fuel = payload / 5

    while True:
        new_fuel = (payload + fuel) / 5

        if new_fuel - fuel < 1:
            return round(new_fuel, 1)

        fuel = new_fuel

    return fuel
