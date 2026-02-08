# 08-02-2026 | 09-02-2026

def calculate_penalty_distance(rounds):
    i=0
    total = 0
    for i in range(len(rounds)):
        if rounds[i] < 5:
            missed = 5 - rounds[i] 
            penalty = missed * 150
            total = penalty + total

    return total
