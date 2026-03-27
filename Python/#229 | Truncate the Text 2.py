#27-03-2026 | 27-03-2026

'''
    Given: string.
    Problem: Truncate a string based on character widths.
                Character widths:
                    - "ilI" → 1
                    - "fjrt" → 2
                    - "abcdeghkmnopqrstuvwxyzJL" → 3
                    - "ABCDEFGHKMNOPQRSTUVWXYZ" → 4
                    - Space (" ") → 2
                    - Period (".") → 1
      Return: If total width ≤ 50, return the string unchanged.
               Otherwise, truncate and append "..." so total width ≤ 60.
'''


def truncate_text(s):
    widths = {}
    widths.update(dict.fromkeys("abcdeghkmnopqrstuvwxyzJL", 3))
    widths.update(dict.fromkeys("ABCDEFGHKMNOPQRSTUVWXYZ", 4))
    widths.update(dict.fromkeys("fjrt", 2))  # override r, t to 2
    widths.update(dict.fromkeys("ilI", 1))
    widths[" "] = 2
    widths["."] = 1

    def char_width(letter):
        return widths.get(letter, 0)

    total_width = 0
    for letter in s:
        total_width += char_width(letter)

    if total_width <= 50:
        return s

    allowed_width = 50 - 3  # reserve width for "..."

    current_width = 0
    result = []
    for letter in s:
        letter_width = char_width(letter)
        if current_width + letter_width > allowed_width:
            break
        result.append(letter)
        current_width += letter_width

    return "".join(result) + "..."


def test_cases():
    print(truncate_text("The quick brown fox"))       # The quick brown f...
    print(truncate_text("The silky smooth sloth"))    # The silky smooth sloth
    print(truncate_text("THE LOUD BRIGHT BIRD"))      # THE LOUD BRIG...
    print(truncate_text("The fast striped zebra"))    # The fast striped z...
    print(truncate_text("The big black bear"))        # The big black bear


if __name__ == "__main__":
    test_cases()
