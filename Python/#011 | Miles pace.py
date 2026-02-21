#21-08-2025 | 09-02-2026

def mile_pace(miles, duration):

    #hrs=hours, mins=minutes
    hrs, mins = map(int,duration.split(":"))
    total_mins = mins + (hrs*60)
    perMile = total_mins / miles

    #time converting
    hrs = int(perMile // 60)
    mins = int(perMile % 60)

    PMduration = f"{hrs:02d}:{mins:02d}" #per mile duration

    return PMduration
