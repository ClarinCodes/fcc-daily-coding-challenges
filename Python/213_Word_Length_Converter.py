#11-03-2026 | 11-03-2026

''' problem: return the len of each words in given string
    example: convert_words("Thanks and happy coding") should return "6 3 5 6"
'''


def convert_words(s):
    words = s.split(" ")
    lengths = []

    for word in words:
        lengths.append(str(len(word)))

    return " ".join(lengths)
