#03-04-2026 | 03-04-2026

'''
    Args: commands (list of str): A list of browser commands.
            each command can be:
            - A URL string (e.g., "example.com")
            - "Back" to go to the previous page
            - "Forward" to go to the next page
    Problem: simulate browser navigation(forward and back).
    Return: list of history and index of current page.
'''


def get_browser_history(commands):
    history = []
    current = -1 # -1 because no page has been visited yet

    for cmd in commands:
        if cmd == "Back":
            if current > 0:
                current -= 1

        elif cmd == "Forward":
            if current < len(history) - 1:
                current += 1

        else:  # URL
            # remove forward history
            history = history[:current + 1]
            history.append(cmd)
            current += 1

    return [history, current]

def test_cases():
    # Test case 1
    assert get_browser_history(["freecodecamp.org", "freecodecamp.org/learn", "Back"]) == [["freecodecamp.org", "freecodecamp.org/learn"], 0]

    # Test case 2
    assert get_browser_history(["example.com", "example.com/about", "example.com/contact", "example.com/blog"]) == [["example.com", "example.com/about", "example.com/contact", "example.com/blog"], 3]

    # Test case 3
    assert get_browser_history(["example.com", "example.com/about", "Back", "Back"]) == [["example.com", "example.com/about"], 0]

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
