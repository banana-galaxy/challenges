def matrixSum(matrix):
    rows, cols = len(matrix), len(matrix[0])
    count = sum(matrix[0])
    for i in range(1, rows):
        for j in range(cols):
            if matrix[i-1][j] != 0:
                count += matrix[i][j]
    return count