
#25-02-2026 | 25-02-2025

''' problem: find the differences between each element, the last element doesn't have the next element to find diff so it is considered as 0.
    given: array with n number of integers.
    return: array diff (current_element - next_element) ends with 0. '''


def find_differences(arr):
    new_arr = []
    for i in range(len(arr)-1): #len(array) - 1, the last element will be 0.
        new_arr.append(arr[i+1] - arr[i])
    new_arr.append(0)
    return new_arr

