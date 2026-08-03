#03-08-2026 | 03-08-2026

def get_emoji_phrase(s):
    emoji_map = {
        "👶": "baby",
        "🐱": "cat",
        "🐕": "dog",
        "🐟": "fish",
        "🥵": "hot",
        "🧊": "ice",
        "🪨": "rock",
        "🦈": "shark",
        "🍲": "soup",
        "⭐": "star"
    }

    return " ".join(emoji_map[emoji] for emoji in s)
