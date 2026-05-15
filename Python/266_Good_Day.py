#03-05-2026 | 03-05-2026


'''
    Problem:
            greeting according to the time.

    Args:
            s (str): time in "HH:MM" format.
    
    Return:
            "Good morning" if times 05:00 to 11:59
            "Good afternoon" if times 12:00 to 17:59
            "Good evening" if times 18:00 to 21:59
            "Good night" if times 22:00 to 04:59

'''

def get_greeting(s):

    hours = int(s.split(":")[0])
    
    if 5 <= hours <= 11:
        return "Good morning"
    elif 12 <= hours <= 17:
        return "Good afternoon"
    elif 18 <= hours <= 21:
        return "Good evening"
    else:
        return "Good night"