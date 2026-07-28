# 28-07-2026 | 28-07-2026

def get_contrast_rating(ratio, is_large_text):
    ratio = float(ratio)

    if is_large_text:
        if ratio >= 4.5:
            return "AAA"
        elif ratio >= 3:
            return "AA"
        else:
            return "Fail"
    else:
        if ratio >= 7:
            return "AAA"
        elif ratio >= 4.5:
            return "AA"
        else:
            return "Fail"
