#14-05-2026 | 14-05-2026

'''
    Problem:
        Check whether s2 is the mirror image of s1. A mirror image is formed by
        reversing s1 and replacing characters with their mirror counterparts.

    Args:
        s1 (str): First input string.
        s2 (str): String to compare against mirror image of s1.

    Return:
        bool: True if s2 is the mirror image of s1, otherwise False.
'''


def is_mirror_image(s1, s2):
    mirror = str.maketrans({
        '[': ']',
        ']': '[',
        '{': '}',
        '}': '{',
        '<': '>',
        '>': '<',
        '(': ')',
        ')': '(',
        'b': 'd',
        'd': 'b',
        'p': 'q',
        'q': 'p'
    })
    
    return s2 == s1[::-1].translate(mirror)



def test_cases():
    assert is_mirror_image("TIM", "TIM") == False
    assert is_mirror_image("{WOW}", "}WOW{") == False
    assert is_mirror_image("XXVII", "IIV%X") == False
    assert is_mirror_image("><(((*>", "<*)))><") == True
    assert is_mirror_image("WTYUIOHAXVMwoxv08=+:|-_*^!.[]{}<>bdpq()",
                            "()pqbd<>{}[].!^*_-|:+=80vxowMVXAHOIUYTW") == True

    print("All test cases passed")


if __name__ == "__main__":
    test_cases()
