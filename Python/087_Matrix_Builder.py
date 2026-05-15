#05-11-2025 | 05-03-2026

''' build matrix '''

def build_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):  
            row.append(0)
        matrix.append(row)
    return matrix
