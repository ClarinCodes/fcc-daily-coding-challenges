# 06-10-2026 | 29-05-2026

"""
    Problem:
        Given an array of distances representing a communication route, compute the total time for a message to reach its destination.
            Rules:
                - Message speed: 300,000 km/s
                - Each satellite (each intermediate node) adds a 0.5 second delay

    Args:
        route (List[int]): Distances along the route

    Return:
        float: Total transmission time, rounded to 4 decimals with trailing zeros removed
"""

def send_message(route):

    total_time = sum(route) / 300000
    total_time += (len(route) - 1) * 0.5

    return float(f"{total_time:.4f}")


def test_cases():
    assert send_message([300000, 300000, 300000]) == 4
    assert send_message([300000]) == 1
    assert send_message([150000, 150000]) == 1.5
    assert send_message([600000, 300000]) == 3.5
    assert send_message([0]) == 0

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
