# 20-03-2026 | 20-03-2026

'''
	Given: time "HH:MM" in 24 hours format.
	Problem: find the shadow cast by a 4-foot vertical pole. 
			  rules:
					-The sun rises at 6am directly "east", and sets at 6pm directly "west".
					-The shadow's length (in feet) is the number of hours away from noon, cubed.
					-There is no shadow before sunrise (before 6am), after sunset (6pm or later), or at noon.
					-Return int or float based on the value.

	Example: given "10:00", return "8ft west" because 10am is 2 hours from noon(12:00), so 2**3 = 8 feet,
				and the shadow points west because the sun is in the east at 10am.
'''

def get_shadow(time):
    hours, minutes = map(int, time.split(":"))
    total_time = hours + minutes / 60
    
    if total_time < 6 or total_time >= 18 or total_time == 12:
        return "No shadow"
    
    if total_time < 12:
        shadow_hours = 12 - total_time
        direction = "west"
    else:
        shadow_hours = total_time - 12
        direction = "east"
    
    length = shadow_hours ** 3
    
    if length % 1 == 0:
        return f"{int(length)}ft {direction}"
    else:
        return f"{length}ft {direction}"
