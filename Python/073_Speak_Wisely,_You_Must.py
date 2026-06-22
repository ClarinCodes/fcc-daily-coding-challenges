# 22-10-2026 | 22-06-2026

"""
    Problem:
        Transform a sentence so it sounds like advice from a wise teacher.

    Args:
        sentence (str): A sentence ending with a single punctuation mark.

    Return:
        str: The transformed sentence following the specified rules.
"""


def wise_speak(sentence):
    p = sentence[-1]
    words = sentence[:-1].split()

    targets = {"have", "must", "are", "will", "can"}

    for i, w in enumerate(words):
        if w.lower() in targets:
            break

    front = words[i + 1:]
    back = [w.lower() for w in words[:i + 1]]

    front[0] = front[0].capitalize()

    return " ".join(front) + ", " + " ".join(back) + p



def test_cases():
    assert wise_speak("You must speak wisely.") == "Speak wisely, you must."
    assert wise_speak("You can do it!") == "Do it, you can!"
    assert wise_speak("Do you think you will complete this?") == "Complete this, do you think you will?"
    assert wise_speak("All your base are belong to us.") == "Belong to us, all your base are."
    assert wise_speak("You have much to learn.") == "Much to learn, you have."


if __name__ == "__main__":
    test_cases()
    print("All tests passed!")
