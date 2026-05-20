# 20-05-2026 | 20-05-2026

"""
    Problem:
        Interleave two strings character by character. Append remaining characters if one string is longer.

    Args:
        a (str), b (str): both are input strings. 

    Return:
        str: string formed by alternating the characters. 

    Time Complexity: O(n+m)
    Space Complexity: O(n+m)
"""

def zip_strings(a, b):
    result = []
  
    for i in range(min(len(a), len(b))):
        result.append(a[i])
        result.append(b[i])
      
    result.append(a[len(b):])
    result.append(b[len(a):])

    return "".join(result)


def test_cases():
    assert zip_strings("abc", "123") == "a1b2c3"
    assert zip_strings("acegikmoqsuwy", "bdfhjlnprtvxz") == "abcdefghijklmnopqrstuvwxyz"
    assert zip_strings("day", "night") == "dnaiyght"
    assert zip_strings("python", "javascript") == "pjyatvhaosncript"
    assert zip_strings("feCdCm", "reoeap") == "freeCodeCamp"

    print("All test cases Passed!")


if __name__ == "__main__":
    test_cases()
