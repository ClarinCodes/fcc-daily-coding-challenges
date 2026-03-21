#05-01-2026 | 21-03-2026

'''
    Given: 4 tire pressures in psi and min, max pressure values in bar.
    Problem: convert the min, max pressure values to psi, check each tire pressure with the given values. 1 bar = 14.5038
    Return: "Low" if the tire pressure is below the minimum allowed.
            "Good" if it's between the minimum and maximum allowed.
            "High" if it's above the maximum allowed.
    Example: tire_status([32, 28, 35, 29], [2, 3]) should return ["Good", "Low", "Good", "Low"].
'''


def tire_status(pressures_psi, range_bar):

    min_psi = range_bar[0] * 14.5038
    max_psi = range_bar[1] * 14.5038
    
    result = []
    for pressure in pressures_psi:
        if pressure < min_psi:
            result.append("Low")
        elif pressure > max_psi:
            result.append("High")
        else:
            result.append("Good")
    
    return result
