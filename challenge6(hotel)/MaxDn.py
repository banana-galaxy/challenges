def matrixSum(mat):
    mat_sum = 0
    for i, row in enumerate(mat):
        for j, val in enumerate(row):
            if i == 0:
                mat_sum += val
                continue

            mat_sum += val if mat[i-1][j] != 0 else 0

    return mat_sum