# 21-06-2026 | 21-06-2026

def get_daytime_hours(latitude):
    daylight = 12 + (latitude / 90) * 12

    daylight = round(daylight / 2) * 2
    daylight = int(daylight)

    sunrise = 12 - daylight // 2
    sunset = 12 + daylight // 2

    return ''.join(
        '☀️' if sunrise <= hour < sunset else '🌑'
        for hour in range(24)
    )
