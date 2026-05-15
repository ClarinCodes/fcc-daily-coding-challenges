#15-08-2025 | 29-03-2026

'''
    Given: lowercase string.
    Problem: All letters between the first and last letter must be sorted alphabetically.
'''


def jbelmu(text):
    result = []
    for word in text.split():
        if len(word) <= 2:
            # leave short words as is
            result.append(word)
        else:
            first = word[0]
            last = word[-1]
            middle = sorted(word[1:-1])
            new_word = first + "".join(middle) + last
            result.append(new_word)
    return " ".join(result)

def test_cases():
    print(jbelmu("hello world"))    # hello wlord
    print(jbelmu("i love jumbled text"))    # i love jbelmud text
    print(jbelmu("freecodecamp is my favorite place to learn to code")) # faccdeeemorp is my faiortve pacle to laern to cdoe
    print(jbelmu("the quick brown fox jumps over the lazy dog"))    # the qciuk borwn fox jmpus oevr the lazy dog

if __name__ == "__main__":
    test_cases()
