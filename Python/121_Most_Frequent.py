# 09-12-2025 | 28-05-2026


"""
    Problem:
        Find the most frequently appearing element in a list.

    Args:
        arr (list): Input list containing elements of any data type.

    Returns:
        element: The element that appears most frequently in the list.
"""


def most_frequent(arr):

    freq = {}                   # Time Complexity: O(n)
                                # Space Complexity: O(k)
    for i in arr:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1

    return max(freq, key=freq.get)
    

    # OR

    # return max(arr, key=arr.count)    # Time Complexity: O(n^2)
                                        # Space Complexity: O(1)
