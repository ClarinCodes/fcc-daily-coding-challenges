# 02-08-2026 | 02-08-2026

def get_food_chain(pairs):

    food_chain = dict(pairs)
    # Example: {"wolf": "deer", "deer": "grass"}

    start = next(predator for predator, prey in pairs
                 if predator not in food_chain.values())

    result = []

    while start:
        result.append(start)
        start = food_chain.get(start)

    return result
