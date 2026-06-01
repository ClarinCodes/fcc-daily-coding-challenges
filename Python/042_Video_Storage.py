# 21-09-2025 | 02-06-2026

"""
    Problem:
        Calculate how many videos can fit on a hard drive.

    Args:
        video_size (int): Size of a single video.
        video_unit (str): Unit of video size (e.g., B, KB, MB, GB, TB).
        drive_size (int): Size of the hard drive.
        drive_unit (str): Unit of hard drive size (e.g., B, KB, MB, GB, TB).

    Returns:
        int: Maximum number of whole videos that can fit on the drive.
"""

def number_of_videos(video_size, video_unit, drive_size, drive_unit):

    if drive_unit not in ["GB", "TB"]:
        return "Invalid drive unit"
    
    if video_unit not in ["B", "KB", "MB", "GB"]:
        return "Invalid video unit"

    unit_map = {
        "B": 1,
        "KB": 1000,
        "MB": 1000 ** 2,
        "GB": 1000 ** 3,
        "TB": 1000 ** 4
    }

    video_bytes = video_size * unit_map[video_unit]
    drive_bytes = drive_size * unit_map[drive_unit]

    return drive_bytes // video_bytes 
