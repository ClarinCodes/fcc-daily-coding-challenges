#16-04-2026 | 16-04-2026 


'''
    Problem:
        Given a string containing numbers and characters, perform operations between numbers based on how many
        non-digit characters lie between them.
        Rules:
        - Even gap → addition
        - Odd gap → subtraction
        - Numbers can be multi-digit
        - Left to right evaluation

    Args:
        s (str): input string

    Returns:
        int: final computed result.
'''


def do_math(s):
    nums = []
    parts = []
    i = 0
    n = len(s)

    # extract numbers and their positions
    while i < n:
        if s[i].isdigit():
            num = 0
            start = i

            # build full number (handles multi-digit)
            while i < n and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1

            nums.append(num)
            parts.append((start, i - 1))
        else:
            i += 1

    # calculations
    result = nums[0]

    for j in range(1, len(nums)):
        prev_end = parts[j - 1][1]
        curr_start = parts[j][0]

        gap = curr_start - prev_end - 1

        if gap % 2 == 0:
            result += nums[j]
        else:
            result -= nums[j]

    return result


def test_cases():
    assert do_math("3ab10c8") == 5
    assert do_math("6MINUS4") == 2
    assert do_math("9plus3") == 12
    assert do_math("5fkwo#10i#%.<>15P=@20!#B/25") == 15
    assert do_math("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt") == 67

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()