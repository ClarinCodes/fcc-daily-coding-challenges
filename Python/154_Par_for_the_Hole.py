#11-01-2026 | 02-05-2026

'''
    Problem:
            return golf scoring label bases on strokes vs bars.
            
    Args:
         par (int) - expected strokes
         strokes (int) - number of strokes taken.

    Return: 
           str - golf scoring label.
'''


def golf_score(par, strokes):

    if strokes == 1:
        return "Hole in one!"

    diff = strokes - par

    score_map = {
        -2: "Eagle",
        -1: "Birdie",
         0: "Par",
         1: "Bogey",
         2: "Double bogey"
    }

    return score_map.get(diff, "Other")