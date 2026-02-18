#17-02-2026 | 18-02-2026

def check_eligibility(athlete_weights, sled_weight):
    persons = len(athlete_weights)
    total_weights = sum(athlete_weights) + sled_weight
    if persons == 1:
        if sled_weight >= 162 and total_weights <= 247:
            return "Eligible"
        else:
            return "Not Eligible"

    elif persons == 2:
        if sled_weight >= 170 and total_weights <= 390:
            return "Eligible"
        else:
            return "Not Eligible"


    elif persons == 4:
        if sled_weight >= 210 and total_weights <= 630:
            return "Eligible"
        else:
            return "Not Eligible"
                
    else:
        return "Not Eligible"

