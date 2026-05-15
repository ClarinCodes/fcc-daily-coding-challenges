#18-09-2025 | 04-05-2026


'''
    Problem:
            Given the size of a fuel tank, the current fuel level, and the price per gallon.
    
    Args:
            All values in int.

    Return: 
            "$d.pp" (str) - the cost to fill the tank fully.
            
'''

def cost_to_fill(tank_size, fuel_level, price_per_gallon):          # fuel_level --> current level
    
    return f"${(tank_size - fuel_level) * price_per_gallon:.2f}"