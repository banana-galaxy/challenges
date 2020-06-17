def matrixSum(mat):
    safe = []
    for i in range(len(mat[0])):
        safe.append(True)
    sum = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0 or not safe[j]:
                safe[j] = False
            else:
                sum += mat[i][j]
    return sum