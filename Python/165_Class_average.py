# 22-01-2026 | 21-02-2026

''' given: a list of scores
    problem: find the avg and return grade
    example: get_average_grade([63, 69, 65, 66, 71, 64, 65]) should return "D".
    why decimal values? some test case return values in decimal, which 66.99 < 67. round() changes the avg score value to high or low.
'''

def get_average_grade(scores):
    average = sum(scores)/len(scores)
    
    if 97 <= average <= 100:
        return "A+"
    elif 93 <= average <= 96.99:
        return "A"
    elif 90 <= average <= 92.99:
        return "A-"
    elif 87 <= average <= 89.99:
        return "B+"
    elif 83 <= average <= 86.99:
        return "B"
    elif 80 <= average <= 82.99:
        return "B-"
    elif 77 <= average <= 79.99:
        return "C+"
    elif 73 <= average <= 76.99:
        return "C"
    elif 70 <= average <= 72.99:
        return "C-"
    elif 67 <= average <= 69.99:
        return "D+"
    elif 63 <= average <= 66.99:
        return "D"
    elif 60 <= average <= 62.99:
        return "D-"
    else:
        return "F"
