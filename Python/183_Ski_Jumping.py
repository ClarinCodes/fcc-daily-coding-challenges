#09-02-2026 | 10-02-2026

# Assigns medals by ranking total score against top three competitors in descending order 
def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):
    total_scr = distance_points + style_points + wind_comp + k_point_bonus
    exist_scr=[165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0]
    exist_scr.sort(reverse=True)
  
    if exist_scr[0] < total_scr:
        return "Gold"
    elif exist_scr[1] < total_scr:
        return "Silver"
    elif exist_scr[2] < total_scr:
        return "Bronze"
    else:
        return "No Medal"
