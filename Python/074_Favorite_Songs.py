# 23-10-2025 | 23-06-2026

"""
    Problem:
        Find the two most played songs from the playlist.

    Args:
        playlist (list[dict]):
            Each dictionary contains:
                - "title" (str): title of the song
                - "plays" (int): number of times the song was played

    Return:
        list[str] : Titles of the two most played songs, in descending order of plays.
"""

def favorite_songs(playlist):

    songs = { }
    for song in playlist:
        title = song["title"]
        plays = song["plays"]

        songs[title] = plays

    top_2 = sorted(songs, key=songs.get, reverse=True)[:2]

    return top_2

def test_cases():
    assert favorite_songs([
        {"title": "Sync or Swim", "plays": 3},
        {"title": "Byte Me", "plays": 1},
        {"title": "Earbud Blues", "plays": 2}
    ]) == ["Sync or Swim", "Earbud Blues"]

    assert favorite_songs([
        {"title": "Skip Track", "plays": 98},
        {"title": "99 Downloads", "plays": 99},
        {"title": "Clickwheel Love", "plays": 100}
    ]) == ["Clickwheel Love", "99 Downloads"]

    assert favorite_songs([
        {"title": "Song A", "plays": 42},
        {"title": "Song B", "plays": 99},
        {"title": "Song C", "plays": 75}
    ]) == ["Song B", "Song C"]

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
