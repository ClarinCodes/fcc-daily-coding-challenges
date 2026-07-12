# 12-07-2026 | 12-07-2026

"""
    Problem:
        Given two zodiac sign strings, return their compatibility
        percentage based on the shortest distance between them on
        the zodiac wheel.

        Zodiac order:
        Aries, Taurus, Gemini, Cancer, Leo, Virgo,
        Libra, Scorpio, Sagittarius, Capricorn,
        Aquarius, Pisces

        Compatibility by shortest distance:
        0 -> "100%"
        1 -> "40%"
        2 -> "80%"
        3 -> "30%"
        4 -> "90%"
        5 -> "20%"
        6 -> "50%"

    Args:
        sign1 (str): The first zodiac sign.
        sign2 (str): The second zodiac sign.

    Return:
        str: The compatibility percentage as a string.
"""

def horoscope_match(sign1, sign2):

    zodiac = [
        "Aries", "Taurus", "Gemini", "Cancer",
        "Leo", "Virgo", "Libra", "Scorpio",
        "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]

    comp = {
        0: "100%",
        1: "40%",
        2: "80%",
        3: "30%",
        4: "90%",
        5: "20%",
        6: "50%"
    }

    i = zodiac.index(sign1)
    j = zodiac.index(sign2)

    distance = abs(i - j)
    distance = min(distance, 12 - distance)

    return comp[distance]
