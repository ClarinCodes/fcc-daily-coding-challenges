#08-12-2025 | 18-03-2026

'''
    Given: value of pound(s)
    Problem: convert pounds into kilograms
    Return: string with both values and singular or plural.
    Example: convert_to_kgs(1) should return "1 pound equals 0.45 kilograms."
'''

def convert_to_kgs(lbs):
    kg = lbs * 0.453592

    p_unit = "pound" if lbs == 1 else "pounds"
    k_unit = "kilogram" if round(kg, 2) == 1.0 else "kilograms"
    
    return f"{lbs} {p_unit} equals {kg:.2f} {k_unit}."
