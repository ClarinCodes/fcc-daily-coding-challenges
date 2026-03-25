#25-03-2026 | 25-03-2026

'''
    Given: current time and finish time of exam in "YYYY-MM-DDTHH:MM:SS" format.
    Problem: compute the time difference between current time and finish time.
    Return: True if the difference is at least 48 hours, otherwise False.
'''

from datetime import datetime, timedelta

def can_retake(finish_time, current_time):
    fmt = "%Y-%m-%dT%H:%M:%S"  # format pattern matching "YYYY-MM-DDTHH:MM:SS"

    # Convert strings to datetime objects
    finish_dt = datetime.strptime(finish_time, fmt)
    current_dt = datetime.strptime(current_time, fmt) 

    time_diff = current_dt - finish_dt

    return time_diff >= timedelta(hours=48)  # True if difference is 48 hours or more

# Test cases
def test_cases():
    print(can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00"))  # True
    print(can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00"))  # False
    print(can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00"))  # True
    print(can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59"))  # False

if __name__ == "__main__":
    test_cases()
