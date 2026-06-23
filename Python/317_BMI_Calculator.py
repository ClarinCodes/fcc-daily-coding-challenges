# 23-06-2026 | 23-06-2026

"""
    Problem:
        Calculate BMI (Body Mass Index).

    Args:
        weight (int) - In pounds.
        height (int) - In inches.

    Return:
        float - BMI of the given with one decimal.


    
    Formulas:
        kg + cm:
            BMI = weight_kg / ((height_cm / 100) ** 2)

        kg + ft:
            BMI = weight_kg / ((height_ft * 0.3048) ** 2)

        lbs + ft:
            BMI = (weight_lbs / ((height_ft * 12) ** 2)) * 703

        lbs + cm:
            BMI = (weight_lbs * 0.45359237) / ((height_cm / 100) ** 2)

"""

def calculate_bmi(weight, height):

    return round((weight / height ** 2) * 703, 1)
