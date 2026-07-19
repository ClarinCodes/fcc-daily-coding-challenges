# 19-07-2026 | 19-07-2026

def elevator_stops(current_floor, requested_floors):
    below = []
    above = []

    for floor in requested_floors:
        if floor < current_floor:
            below.append(floor)
        else:
            above.append(floor)

    below.sort(reverse=True)
    above.sort()

    if len(below) > 0:
        down_distance = current_floor - below[-1]
        if len(above) > 0:
            down_distance += above[-1] - below[-1]
    else:
        down_distance = None

    if len(above) > 0:
        up_distance = above[-1] - current_floor
        if len(below) > 0:
            up_distance += above[-1] - below[-1]
    else:
        up_distance = None

    if down_distance is not None and ( up_distance is None or down_distance <= up_distance):
        return below + above
    else:
        return above + below
