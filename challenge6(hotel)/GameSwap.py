def matrixSum(matrix):
    sum = 0
    for j in range(len(matrix[0])):
        for array in matrix:
            if array[j] == 0:
                break
            else:
                sum += array[j]
    print(sum)