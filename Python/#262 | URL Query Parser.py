#29-04-2026 | 29-04-2026

'''
    Problem:
        Parse the query string of a URL into a dictionary of key-value pairs.
    
    Args:
        url (str): A URL containing an optional query string after '?'
    
    Return:
        dict: Dictionary of query where all values are strings.
    
'''

def parse_url_query(url):
    
    if "?" not in url:
        return {}
    
    query_string = url.split("?", 1)[1]
    pairs = query_string.split("&")
    
    result = {}
    
    for pair in pairs:
        if "=" in pair:
            key, value = pair.split("=", 1)
            result[key] = value
    
    return result