def matrixSum(matrix):
    Sum = 0
    col = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                col.append(j)
            if i == 0:
                Sum += matrix[i][j]
            if matrix[i][j] != 0 and i < len(matrix)-1 and j not in col:
                Sum += matrix[i+1][j]
            
    return Sum