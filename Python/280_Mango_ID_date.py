#17-05-2026 | 17-05-2026

'''
    Problem:
            Given a MongoDB ID string, return its creation timeas an ISO 8601 string.

            A MongoDB ID is a 24-character hex string.
            The first 8 characters represent a Unix timestamp encoded in hexadecimal.

    Args:
            mongo_id (str): A 24-character MongoDB ObjectId string.

    Return:
            str: ISO 8601 formatted UTC date string.
'''


from datetime import datetime, timezone
def mongo_id_to_date(mongo_id):

    # Take first 8 characters (hex timestamp)
    timestamp_hex = mongo_id[:8]

    # Convert hex -> integer
    timestamp = int(timestamp_hex, 16)

    # Convert timestamp -> UTC datetime
    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)

    # Return ISO 8601 format
    return dt.isoformat(timespec='milliseconds').replace('+00:00', 'Z')


def test_cases():
    print(mongo_id_to_date("6a094b50bcf86cd799439011"))
    # 2026-05-17T05:00:00.000Z

    print(mongo_id_to_date("695344eb1f4a4c1123042128"))
    # 2025-12-30T03:20:11.000Z

    print(mongo_id_to_date("386da62df34123ac54617e56"))
    # 2000-01-01T07:01:01.000Z

    print(mongo_id_to_date("69f571c3d7711807afd3dd55"))
    # 2026-05-02T03:38:43.000Z

    print(mongo_id_to_date("68adce01c0e1144d0a90295a"))
    # 2025-08-26T15:08:49.000Z


if __name__ == "__main__":
    test_cases()
