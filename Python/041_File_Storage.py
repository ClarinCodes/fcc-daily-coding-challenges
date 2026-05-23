# 20-09-2025 | 23-05-2026

"""
    Problem:
        Given a file size, a unit for the file size, and hard drive capacity in gigabytes (GB), determine how many whole files can fit on the hard drive.
            The file size unit can be:
            - "B" (bytes)    
            - "KB" (kilobytes)
            - "MB" (megabytes)

        Use decimal conversions:
        1 KB = 1000 B
        1 MB = 1000 KB
        1 GB = 1000 MB

    Example:
        Input: file_size = 500, file_unit = "KB", drive_size_gb = 1
        Output: 2000


    Args:
        file_size (int): Size of a single file in the given unit.
        file_unit (str): Unit of the file size ("B", "KB", or "MB").
        drive_size_gb (int or float): Capacity of the hard drive in gigabytes.

    Return:
        int: Number of whole files that can fit on the hard drive.
"""

def number_of_files(file_size, file_unit, drive_size_gb):

    size = {
        "B": 1,
        "KB": 1000,
        "MB": 1000**2,
        "GB": 1000**3
    }

    file_size_b = file_size * size[file_unit]
    drive_size_b = drive_size_gb * size["GB"]

    return drive_size_b // file_size_b
