# 03-07-2026 | 03-07-2026

def migrate_record(schema, record):

    result = record.copy()
    
    for key, value in schema.items():
        if key not in result:
            result[key] = value
            
    return result
