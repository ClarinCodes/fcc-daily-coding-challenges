# 25-05-2026 | 25-05-2026

def guess_number(secret, guess):

    if secret > guess:
        return "higher"
    elif secret < guess:
        return "lower"
    else:
        return "you got it!"
