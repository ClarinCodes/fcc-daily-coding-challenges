# 31-10-2025 | 04-06-2026

"""
    'hello_world' should return HeLlO~wOrLd
"""

def spookify(boo):
    spooky = []
    upper = True

    for c in boo:
        if c in "_-":
            spooky.append("~")

        elif c.isalpha():
            spooky.append(c.upper() if upper else c.lower())
            upper = not upper
            
        else:
            spooky.append(c)

    return ''.join(spooky)
