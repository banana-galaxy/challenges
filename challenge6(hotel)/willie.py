def matrixSum(matrix):
    sum = 0
    badCols = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if column in badCols:
                continue

            if matrix[row][column] == 0:
                badCols.append(column)     
            
            sum += matrix[row][column]
            

    return sum