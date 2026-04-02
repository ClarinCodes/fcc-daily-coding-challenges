#02-04-2026 | 02-04-2026

'''
    Given: string.
    Problem: capitalizes characters in a string whose indices are Fibonacci numbers.
             non-Fibonacci indices are lowercased. Non-letter characters remain unchanged.
    Return:  Transformed string with Fibonacci-indexed letters capitalized.
'''


def capitalize_fibonacci(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    fib = set()
    first, second = 0, 1

    while first < len(s):
        fib.add(first)
        first, second = second, first + second

    output = []

    for i, char in enumerate(s):
        if i in fib:
            if char.isalpha():
                output.append(char.upper())
            else:
                output.append(char)
        else:
            output.append(char.lower())

    return ''.join(output)


def test_cases():
    assert capitalize_fibonacci("hello world") == "HELLo woRld"
    assert capitalize_fibonacci("HELLO WORLD") == "HELLo woRld"
    assert capitalize_fibonacci("hello, world!") == "HELLo, wOrld!"
    assert capitalize_fibonacci("The quick brown fox jumped over the lazy dog.") == "THE qUicK broWn fox jUmped over thE lazy dog."
    print("Test cases Passed")
    

if __name__ == "__main__":
    test_cases()
