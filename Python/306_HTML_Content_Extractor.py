# 12-06-2026 | 12-06-2026

"""

    Problem:
        Convert the HTML code string into plain text.

    Args:
        html (str) : HTML string.

    Return:
        str : Plain text.

"""

import re

def extract_content(html):
    return re.sub(r'<[^>]+>', '', html)

print(extract_content('<p>hello world</p>'))
