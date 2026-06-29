# 21-06-2026 | 21-06-2026

"""
    Problem:
        Determine the mood of a song based on its genre and BPM.
                +---------+--------------+-----------+
                | Mood    | Genre        | BPM Range |
                +---------+--------------+-----------+
                | focus   | classical    | 60–109    |
                | focus   | electronic   | 60–89     |
                | happy   | pop          | 60–180    |
                | happy   | classical    | 110–180   |
                | happy   | rock         | 60–129    |
                | happy   | electronic   | 90–134    |
                | hype    | rock         | 130–180   |
                | hype    | electronic   | 135–180   |
                +---------+--------------+-----------+

    Args:
        genre (str): The song's genre.
        bpm (int): The song's tempo in beats per minute.

    Return:
        str: Matching mood, or None if no match exists.
"""


def get_mood(genre, bpm):
    if genre == "classical":
        return "focus" if bpm < 110 else "happy" if bpm <= 180 else None

    elif genre == "electronic":
        if bpm < 90:
            return "focus"
        if bpm < 135:
            return "happy"
        return "hype" if bpm <= 180 else None

    elif genre == "pop":
        return "happy" if 60 <= bpm <= 180 else None

    elif genre == "rock":
        return "happy" if bpm < 130 else "hype" if bpm <= 180 else None

    return None
