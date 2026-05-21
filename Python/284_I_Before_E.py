# 21-05-2026 | 21-05-2026

"""
    Problem:
        Swap the letters "i" and "e" according to the rule:
            1. Replace "ei" with "ie" if it is not preceded by "c".
            2. Replace "ie" with "ei" if it is preceded by "c".
        All other words are left unchanged.

    Args:
        sentence (str): Input string containing incorrectly ordered letters.

    Returns:
        str: Corrected string.
"""


def i_before_e(sentence):

    words = sentence.split()

    for w in range(len(words)):
        word = list(words[w])

        for i in range(len(word) - 1):
            if word[i] == "e" and word[i + 1] == "i" and (i == 0 or word[i - 1] != "c"):
                word[i], word[i + 1] = "i", "e"

            elif word[i] == "i" and word[i + 1] == "e" and i > 0 and word[i - 1] == "c":
                word[i], word[i + 1] = "e", "i"

        words[w] = "".join(word)

    return " ".join(words)


def test_cases():
    assert i_before_e("beleive") == "believe"
    assert i_before_e("recieve") == "receive"
    assert i_before_e("we recieved a breif") == "we received a brief"

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
