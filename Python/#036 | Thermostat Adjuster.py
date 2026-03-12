#15-09-2025 | 12-03-2026

''' Give: the current temperature of a room and a target temperature.

          Return "heat" if the current temperature is below the target.
          Return "cool" if the current temperature is above the target.
          Return "hold" if the current temperature is equal to the target.
'''

def adjust_thermostat(temp, target):
    if temp < target:
        return "heat"
    elif temp > target:
        return "cool"
    else:
        return "hold"
