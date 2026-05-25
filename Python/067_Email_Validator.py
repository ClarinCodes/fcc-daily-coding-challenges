# 16-10-2025 | 25-05-2026

  """
    Problem:
        Validate whether a given string is a valid email address based on specific rules.

        Rules:
        - Must contain exactly one '@' symbol.
        - Local part (before '@'):
            * Can contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), and hyphens (-).
            * Cannot start or end with a dot.
            * Cannot contain two consecutive dots.
        - Domain part (after '@'):
            * Must contain at least one dot.
            * Must not contain two consecutive dots.
            * Must end with a dot followed by at least two letters.

    Args:
        email (str): The email string to be validated.

    Return:
        bool: True if the email is valid, False otherwise.
    """


import re
# `re` is Python’s module for working with regular expressions to search, match, and manipulate text patterns.

def validate(email):

    if email.count("@") != 1:
        return False

    local, domain = email.split("@")

    if local.startswith(".") or local.endswith("."):
        return False

    if ".." in local or ".." in domain:
        return False

    if not re.fullmatch(r"[A-Za-z0-9._-]+", local):
        return False

    if "." not in domain:
        return False

    # domain ending: . + at least 2 letters
    if not re.search(r"\.[A-Za-z]{2,}$", domain):
        return False

    return True
