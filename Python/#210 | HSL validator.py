#08-03-2026 | 08-03-2026

'''
Given: a string representing a CSS HSL color value.
Problem: determine whether the string is a valid HSL color.

Rules for a valid HSL value:
    - Must be in the format "hsl(h, s%, l%)"
    - h (hue) must be a number between 0 and 360 inclusive
    - s (saturation) must be a percentage between 0% and 100%
    - l (lightness) must be a percentage between 0% and 100%
    - Spaces are allowed:
         * After the opening parenthesis
         * Before and/or after the commas
         * Before and/or after the closing parenthesis
    - Optionally, the string can end with a semicolon (";")

Returns True if the HSL string is valid, otherwise False.

Example:
    is_valid_hsl("hsl(240, 50%, 50%)") -> True
    is_valid_hsl("hsl(200, 55%, 75)")  -> False
    is_valid_hsl("hsl (80, 20%, 10%)") -> False
'''


def is_valid_hsl(hsl):
    # reject space between hsl and (
    if not hsl.startswith("hsl("):
        return False

    lis = hsl.replace("hsl(","").replace("%","").replace(")","").replace(";","")

    #check that saturation and lightness actually have %
    parts = hsl[hsl.find("(")+1 : hsl.rfind(")")].split(",")
    if not parts[1].strip().endswith("%") or not parts[2].strip().endswith("%"):
        return False

    hue, saturation, lightness = map(int, lis.split(","))

    if (hue >= 0 and hue <= 360) and (saturation >=0 and saturation <= 100) and (lightness >= 0 and lightness <= 100):
        return True
    else:
        return False
