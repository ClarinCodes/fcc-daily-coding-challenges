# 16-09-2026 | 18-09-2026 

"""
    Capitalize first word of every sentences. each sentence ends with [., ?, !].
"""

def capitalize(paragraph):
    result = ""
    capitalize_next = True

    for char in paragraph:
        if capitalize_next and char.isalpha():
            result += char.upper()
            capitalize_next = False
        else:
            result += char

        if char in ".?!":
            capitalize_next = True

    return result
