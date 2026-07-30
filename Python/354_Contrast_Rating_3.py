# 30-07-2026 | 30-07-2026

def get_contrast_rating(rgb1, rgb2, is_large_text):
    def luminance(rgb):
        values = []

        for c in rgb:
            c = c / 255
            if c <= 0.04045:
                c = c / 12.92
            else:
                c = ((c + 0.055) / 1.055) ** 2.4
            values.append(c)

        return 0.2126 * values[0] + 0.7152 * values[1] + 0.0722 * values[2]

    l1 = luminance(rgb1)
    l2 = luminance(rgb2)

    ratio = (l1 + 0.05) / (l2 + 0.05)

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
