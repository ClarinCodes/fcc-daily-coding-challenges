#28-04-2026 | 28-04-2026

'''
        Problem: Given an integer n from 0 to 99, return its English word representation.
                    Rules:
                          - 0-19 have unique names.
                          - Multiples of 10 (20-90) have their own names.
                          - Other numbers are written as two words joined by a hyphen (e.g., "forty-two").
        
        Args: n (int) - an integer between 0 to 99.

        Return: str - English word representation of given int.

'''



def get_number_words(n):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "eleven", "twelve", "thirteen",
            "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
            "nineteen"]

    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    if n < 20:
        return ones[n]

    if n % 10 == 0:
        return tens[n // 10]

    # 21–99 (non-multiples of 10)
    return tens[n // 10] + "-" + ones[n % 10]

def test_cases():
    assert get_number_words(0) == "zero"
    assert get_number_words(7) == "seven"
    assert get_number_words(13) == "thirteen"
    assert get_number_words(20) == "twenty"
    assert get_number_words(42) == "forty-two"
    assert get_number_words(58) == "fifty-eight"
    assert get_number_words(90) == "ninety"
    assert get_number_words(99) == "ninety-nine"
    print("All test cases passed!")

if __name__ == "__main__":
    test_cases()