# 26-10-2025 | 20-07-2026

"
    Problem:
        Convert seconds into duration format "H:MM:SS".
            - seconds: should always be two digits.
            - Minute: "0" if the duration is less than one minute.
    Args:
        seconds (int)

    Return:
        str: in the format of "HH:MM:SS" or "H:MM:SS" or "M:SS".
"

def format(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes}:{secs:02d}"
