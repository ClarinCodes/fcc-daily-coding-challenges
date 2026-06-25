# 25-08-2025 | 25-06-2026

"""
    Problem:
        Convert a string containing words separated by underscores (_),
        hyphens (-), or spaces into camelCase.

    Args:
        s (str): Input string.

    Return:
        str: The camelCase version of the input string.
"""

def to_camel_case(s):

    for sep in "_-":
        s = s.replace(sep, " ")

    words = s.split()

    return words[0].lower() + "".join(
        word.capitalize() for word in words[1:]
    )


def test_cases():
    assert to_camel_case("hello_world") == "helloWorld"
    assert to_camel_case("hello-world") == "helloWorld"
    assert to_camel_case("hello world") == "helloWorld"
    assert to_camel_case("hello_world-test case") == "helloWorldTestCase"
    assert to_camel_case("HELLO_WORLD") == "helloWorld"
    assert to_camel_case("python") == "python"
    assert to_camel_case("___hello---world___") == "helloWorld"
    assert to_camel_case("multiple   spaces") == "multipleSpaces"

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
    
