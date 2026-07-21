# 19-09-2025 | 21-07-2026

"""
    Problem:
        Calculates the maximum number of photos that can be stored on a drive.
        Conversion: 1 GB = 1000 MB.

    Args:
        photo_size_mb (int): Size of a single photo in megabytes (MB).
        drive_size_gb (int): Total capacity of the storage drive in gigabytes (GB).

    Returns:
        int: The maximum number of photos that can be stored.
"""

def number_of_photos(photo_size_mb, drive_size_gb):

    return drive_size_gb * 1000 // photo_size_mb
