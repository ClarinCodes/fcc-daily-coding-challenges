#26-09-2025 | 12-03-2026

'''Given: array of numbers representing the speed of vehicles. speed limit.
   Problem: count the overspeed vehicles and find average excess speed of those vehicles.
   Example: speeding([58, 50, 60, 55], 55) should return [2, 4]
'''

def speeding(speeds, limit):
    avg_excess = 0
    vehicles = 0
    excess_speed = 0
  
    for i in speeds:
        if i > limit:
            vehicles += 1
            excess_speed += i - limit
          
    if vehicles != 0:       # without this causes ZeroDivision error
        avg_excess = excess_speed / vehicles
      
    return [vehicles, avg_excess]
