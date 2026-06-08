# 02-06-2026 | 08-06-2026

def is_valid_schema(obj):
    
    return (
        isinstance(obj.get("username"), str)
        and isinstance(obj.get("verified"), bool)
        and isinstance(obj.get("posts"), int)
    )
