# 29-05-2026 | 29-05-2026

"""
    Problem:
        Given two strings representing image dimensions, return the aspect ratio of the image with the greater width-to-height ratio.

    Args:
        a (str): Image dimensions in format "WxH"
        b (str): Image dimensions in format "WxH"

    Return:
        str: Simplified aspect ratio in format "W:H"
"""

import math

def get_wider_aspect_ratio(a: str, b: str) -> str:
    a_w, a_h = map(int, a.split("x"))
    b_w, b_h = map(int, b.split("x"))

    if a_w * b_h > b_w * a_h:
        divisor = math.gcd(a_w, a_h)
        return f"{a_w // divisor}:{a_h // divisor}"

    divisor = math.gcd(b_w, b_h)
    return f"{b_w // divisor}:{b_h // divisor}"


def test_cases():
    assert get_wider_aspect_ratio("1920x1080", "800x600") == "16:9"
    assert get_wider_aspect_ratio("1080x1350", "2048x1536") == "4:3"
    assert get_wider_aspect_ratio("640x480", "2440x1220") == "2:1"
    assert get_wider_aspect_ratio("360x640", "1080x1920") == "9:16"
    assert get_wider_aspect_ratio("3440x1440", "2048x858") == "43:18"
    assert get_wider_aspect_ratio("12345x61234", "12534x51234") == "2089:8539"

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
