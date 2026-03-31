#31-03-2026 | 31-03-2026

'''
    Given: alarm_time, wake_time: string in "HH:MM" format.

    Problem: Determine whether you woke up early, on time (within 10 minutes of the alarm), or late.

    Return:
        - "early" if woke up before alarm
        - "on time" if woke up at alarm or within 10 minutes after
        - "late" if woke up more than 10 minutes after alarm
'''


def alarm_check(alarm_time, wake_time):
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        wake_hour, wake_minute = map(int, wake_time.split(":"))
    except ValueError:
        raise ValueError("Time must be in HH:MM format with numeric values.")
    
    total_alarm_minutes = alarm_hour * 60 + alarm_minute
    total_wake_minutes = wake_hour * 60 + wake_minute
    minutes_difference = total_wake_minutes - total_alarm_minutes

    if minutes_difference < 0:
        return "early"
    elif 0 <= minutes_difference <= 10:
        return "on time"
    else:
        return "late"

def test_cases():
    print (alarm_check("07:00", "06:45"))    # early
    print (alarm_check("06:30", "06:30"))    # on time
    print (alarm_check("08:10", "08:15"))    # on time
    print (alarm_check("09:30", "09:45"))    # late
    print (alarm_check("08:15", "08:25"))    # on time

if __name__ == "__main__":
    test_cases()
