# 29-07-2026 | 29-07-2026

def get_contrast_rating(lighter, darker, is_large_text):
    ratio = (lighter + 0.05) / (darker + 0.05)

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
