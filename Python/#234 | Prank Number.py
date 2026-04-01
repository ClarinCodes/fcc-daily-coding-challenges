#01-04-2026 | 01-04-2026

'''
    Given: array of numbers in a pattern.
    Problem: find a number that doesn't follow the pattern.
                - it can be increased from one tho the next by amount.
                - it can be decreased, similar to addition.
            change that one number in the array.
    Return: corrected pattern array.
'''


def fix_prank_number(arr):
    diffs = []
    for i in range(1, len(arr)):
        diffs.append(arr[i] - arr[i - 1])

    expected_diff = max(diffs, key=diffs.count)

    if len(arr) > 2:
        if (arr[1] - arr[0] != expected_diff) and (arr[2] - arr[1] == expected_diff):
            arr[0] = arr[1] - expected_diff

    corrected = [arr[0]]
    for i in range(1, len(arr)):
        last = corrected[-1]
        if arr[i] - last == expected_diff:
            corrected.append(arr[i])
        else:
            corrected.append(last + expected_diff)

    return corrected

def test_cases():
    assert fix_prank_number([2, 4, 7, 8, 10]) == [2, 4, 6, 8, 10]
    assert fix_prank_number([10, 10, 8, 7, 6]) == [10, 9, 8, 7, 6]
    assert fix_prank_number([12, 24, 36, 48, 61, 72, 84, 96]) == [12, 24, 36, 48, 60, 72, 84, 96]
    assert fix_prank_number([4, 1, -2, -5, -8, -5]) == [4, 1, -2, -5, -8, -11]
    assert fix_prank_number([0, 100, 200, 300, 150, 500]) == [0, 100, 200, 300, 400, 500]
    assert fix_prank_number([400, 425, 400, 375, 350, 325, 300]) == [450, 425, 400, 375, 350, 325, 300]
    assert fix_prank_number([-5, 5, 10, 15, 20]) == [0, 5, 10, 15, 20]
    print("All test cases passed!")

if __name__ == "__main__":
    test_cases()
