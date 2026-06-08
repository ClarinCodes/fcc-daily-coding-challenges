# 08-06-2026 | 08-06-2026

"""
    Problem:
        Calculate the jet lag hours between two cities based on
        timezone difference, flight duration, and travel direction.

    Args:
        departure_city (str): Departure city.
        arrival_city (str): Arrival city.
        flight_duration (int): Flight duration in hours.
        direction (str): Travel direction ("east" or "west").

    Return:
        float : Jet lag hours rounded to one decimal place.
"""

def get_jet_lag_hours(departure_city, arrival_city, flight_duration, direction):

    cities = {
        "Los Angeles": -8,
        "New York": -5,
        "London": 0,
        "Istanbul": 3,
        "Dubai": 4,
        "Hong Kong": 8,
        "Tokyo": 9
    }

    timezone_diff = cities[arrival_city] - cities[departure_city]

    jet_lag_hours = abs(timezone_diff) + (flight_duration * 0.1) * (1.5 if direction == "east" else 1.0)

    return jet_lag_hours
    

def test_cases():
    assert get_jet_lag_hours("Istanbul", "Hong Kong", 10, "east") == 6.5
    assert get_jet_lag_hours("London", "New York", 8, "west") == 5.8
    assert get_jet_lag_hours("Hong Kong", "Tokyo", 4, "east") == 1.6
    assert get_jet_lag_hours("Dubai", "London", 7, "west") == 4.7
    assert get_jet_lag_hours("Los Angeles", "Hong Kong", 15, "west") == 17.5
    assert get_jet_lag_hours("Tokyo", "Dubai", 9, "west") == 5.9
    assert get_jet_lag_hours("New York", "Istanbul", 10, "east") == 9.5
    print("All tests passed!")

if __name__ == "__main__":
    test_cases()
