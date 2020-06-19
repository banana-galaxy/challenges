def matrixSum(matrix):
    roomOk = matrix
    for arrayNum in range(0, len(matrix)):
        for elementNum in range(0, len(matrix[arrayNum])):
            if matrix[arrayNum][elementNum] == 0:
                for i in range(arrayNum, len(matrix)):
                    roomOk[i][elementNum] = "no"
    flat_list = [item for sublist in roomOk for item in sublist if item != "no"]
    return sum(flat_list)