#22-03-2026 | 22-03-2026 

'''
    Given: string of bean characters (' for light, - for medium, . for dark)
    Problem: calculate the average point value of all beans and determine roast level
              ' = 1 point
              - = 2 points
              . = 3 points
    Return: roast level ("Light", "Medium", or "Dark") based on average points
'''

def detect_roast(beans):
    points = 0 

    for char in beans:
        if char == "'":
            points += 1
        elif char == '-':
            points += 2
        else:
            points += 3

    avg_points = points / len(beans)

    if avg_points < 1.75:
        return "Light"
    elif avg_points > 2.5:
        return "Dark"
    return "Medium"
    
