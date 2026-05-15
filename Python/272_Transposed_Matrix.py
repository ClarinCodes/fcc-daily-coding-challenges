#09-05-2026 | 09-05-2026

'''
    Problem:
            Transpose given matrix.

    Args:
            matrix (2D array) - input values.

    Return:
            2D array (list) - transposed matrix.
'''

def transpose(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)

    return result



def test_cases():
    assert transpose([[1, 2, 3],
                      [4, 5, 6]]) == [[1, 4],
                                       [2, 5],
                                       [3, 6]]

    assert transpose([[1, 2],
                      [3, 4],
                      [5, 6]]) == [[1, 3, 5],
                                   [2, 4, 6]]

    assert transpose([[7]]) == [[7]]

    assert transpose([[1, 2, 3]]) == [[1],
                                       [2],
                                       [3]]

    assert transpose([[1],
                      [2],
                      [3]]) == [[1, 2, 3]]


if __name__ == "__main__":
    test_cases()
    print("All transpose tests passed!")