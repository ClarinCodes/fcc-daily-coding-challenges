# 05-06-2026 | 06-06-2026

def is_valid_schema(obj):

    ROLES = {"user", "creator", "moderator", "staff", "admin"}

    if not isinstance(obj, dict):
        return False

    required = ["username", "posts", "verified", "role", "badges"]

    for key in required:
        if key not in obj:
            return False

    if not isinstance(obj["username"], str):
        return False

    if not isinstance(obj["posts"], int):
        return False

    if not isinstance(obj["verified"], bool):
        return False

    if obj["role"] not in ROLES:
        return False

    if not isinstance(obj["badges"], list):
        return False

    for badge in obj["badges"]:
        if not isinstance(badge, str):
            return False

    if "supporter" in obj and not isinstance(obj["supporter"], bool):
        return False

    return True
