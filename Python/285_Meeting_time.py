# 22-05-2026 | 22-05-2026

"""
    Problem:
        Find the earliest starting hour where all people have a shared availability window of at least one hour. Return "None" if no such hour exists.

    Args:
        availability (list): 3D array of [start, end] integer pairs for each person, (start: 0-23, end: 1-24).

    Return:
        int or str: The earliest shared start hour, or "None".
"""


def get_meeting_time(availability):
    if not availability:
        return "None"
        
    num_people = len(availability)
    hourly_counts = [0] * 24
    
    for person in availability:
        unique_hours_for_person = set()
        
        for start, end in person:
            for hour in range(start, end):
                unique_hours_for_person.add(hour)

        for hour in unique_hours_for_person:
            hourly_counts[hour] += 1

    for hour in range(24):
        if hourly_counts[hour] == num_people:
            return hour
            
    return "None"
