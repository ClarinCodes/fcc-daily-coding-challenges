# 04-06-2026 | 06-06-2026

def is_valid_schema(obj):

    ROLES = {"user", "creator", "moderator", "staff", "admin"}

    if not isinstance(obj, dict):
        return False

    # required fields
    required = ("username", "posts", "verified", "role")

    if any(key not in obj for key in required):
        return False

    username = obj["username"]
    posts = obj["posts"]
    verified = obj["verified"]
    role = obj["role"]

    if not isinstance(username, str):
        return False

    if not isinstance(posts, (int, float)) or isinstance(posts, bool):
        return False  # prevents True/False being treated as numbers

    if not isinstance(verified, bool):
        return False

    if role not in ROLES:
        return False

    if "supporter" in obj and not isinstance(obj["supporter"], bool):
        return False

    return True
