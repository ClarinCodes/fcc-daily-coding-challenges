#02-03-2026 | 02-03-2026

'''Given a string, return the sum of its letters.

Letters are A-Z in uppercase or lowercase
Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
Uppercase and lowercase letters have the same value.
Ignore all non-letter characters.
'''


def sum_letters(s):
    total = 0  # Initialize total sum

    for char in s:
        if char.isalpha():  # Only process letters
            uppercase_char = char.upper()          # Convert to uppercase
            ascii_value = ord(uppercase_char)     # Get ASCII value
            alphabet_position = ascii_value - ord('A') + 1  # Convert to 1–26
            total += alphabet_position            # Add to total

    return total
