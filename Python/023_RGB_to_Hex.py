# 02-09-2026 | 03-09-2026

"""
    Problem:
        Convert CSS rgb string to hexadecimal.

    Args:
        rgb (str)  - in the format of rgb(r, g, b).

    Return:
        str - # followed by hexadecimal values.
"""

def rgb_to_hex(rgb):

    r, g, b = map(int, rgb[4:-1].split(', '))

    return f"#{r:02x}{g:02x}{b:02x}"
