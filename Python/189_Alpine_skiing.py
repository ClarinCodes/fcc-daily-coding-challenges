#15-02-2026 | 15-02-2026

def get_hill_rating(drop, distance, type_):
    steepness = drop / distance
    
    if type_ == 'Slalom':
        player = steepness * 0.9
    elif type_ == 'Downhill': 
        player = steepness * 1.2
    else:
        player = steepness * 1.0
    
    if player <= 0.1:
        return 'Green'
    elif player > 0.1 and player <= 0.25:
        return 'Blue'
    else:
        return 'Black'
