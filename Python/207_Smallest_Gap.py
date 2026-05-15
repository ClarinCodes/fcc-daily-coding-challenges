#05-03-2026 | 17-04-2026


'''
    Problem: Given a string, find the substring between two identical characters
             that have the smallest number of characters between them.
                Rules:
                    - There is always at least one repeating character.
                    - Return the substring between the pair (exclude the matching characters).
                    - If multiple pairs have the same smallest gap, return the first one found.

    Args: s (str): Input string

    Returns: str: Substring between the closest pair of identical characters
'''


def smallest_gap(s):

    last_seen = {}
    min_gap = float('inf')
    result = ""

    for i, ch in enumerate(s):
        if ch in last_seen:
            j = last_seen[ch]
            gap = i - j - 1
            if gap < min_gap:
                min_gap = gap
                result = s[j + 1:i]
        last_seen[ch] = i

    return result


def test_cases():
    assert smallest_gap("ABCDAC") == "DA"
    assert smallest_gap("racecar") == "e"
    assert smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4") == "#q6e&rkf(p"
    assert smallest_gap("Hello World") == ""
    assert smallest_gap("The quick brown fox jumps over the lazy dog.") == "fox"

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()