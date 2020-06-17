def matrixSum(matrix):
    y = len(matrix) # len of list
    if y < 1: #if ^ empty
        return False
    x = len(matrix[0]) #len of lists in list
    skip = [] #columns with 0 to skip
    result = 0 #there goes the sum
    for i in range(y):
        for j in range(x):
            if j in skip: #skip if there was a zero above
                continue
            if matrix[i][j] == 0: #if zero in than add column to skip
                skip.append(j)
                continue
            result += matrix[i][j]
    return result