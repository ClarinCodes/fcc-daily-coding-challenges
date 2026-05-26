# 26-05-2026 | 26-05-2026

"""
    Problem:
        Find the sum of difference between consecutive elements. 
            (a2-a1)+(a3-a2)+...

    Args:
        arr (lst[int]) : List of numbers. 

    Return:
        int : Sum of the difference.

"""

def sum_of_differences(arr):

    diff = 0

    for i in range(len(arr)-1):
        diff += arr[i+1] - arr[i]

    return diff



def test_cases():
    assert sum_of_differences([1, 3, 4]) == 3
    assert sum_of_differences([5, -3, 3, 9, 10]) == 5
    assert sum_of_differences([9, 6, 15, -20, 33, 14, 25, 16, -7]) == -16
    assert sum_of_differences([50, 102, -46, 82, -49, 29, 71, 902, -237, 111, -61, 75]) == 25

    print("All test cases passed!")


if __name__ == "__main__":
    test_cases()
