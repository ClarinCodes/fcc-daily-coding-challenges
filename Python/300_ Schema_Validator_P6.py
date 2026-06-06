# 06-06-2026 | 06-06-2026

def is_valid_schema(obj):

    Roles = {"user", "creator", "moderator", "staff", "admin"}

    # must be dict
    if not isinstance(obj, dict):
        return False

    if "users" not in obj or not isinstance(obj["users"], list):
        return False

    for user in obj["users"]:

        if not isinstance(user, dict):
            return False

        # required fields
        required = ["username", "posts", "verified", "role", "badges"]

        for key in required:
            if key not in user:
                return False

        if not isinstance(user["username"], str):
            return False

        if not isinstance(user["posts"], int):
            return False

        if not isinstance(user["verified"], bool):
            return False

        if user["role"] not in Roles:
            return False

        if not isinstance(user["badges"], list):
            return False

        for b in user["badges"]:
            if not isinstance(b, str):
                return False

        # optional field
        if "supporter" in user and not isinstance(user["supporter"], bool):
            return False

    return True
