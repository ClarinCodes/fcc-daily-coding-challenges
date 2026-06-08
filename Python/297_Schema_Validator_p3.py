# 03-06-2026 | 08-06-2026

def is_valid_schema(obj):

    Roles = ["user", "creator", "moderator", "staff", "admin"] 

    return (
        isinstance(obj.get("username"), str) and
        isinstance(obj.get("posts"), int) and
        isinstance(obj.get("verified"), bool) and
        obj.get("role") in Roles
        )
