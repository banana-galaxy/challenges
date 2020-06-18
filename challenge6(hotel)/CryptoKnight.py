def matrixSum(matrix):
    list_to_sum = []
    for placeholder in range(len(matrix[0])):
        for list_holder in range(len(matrix)):
            if matrix[list_holder][placeholder] != 0:
                list_to_sum.append(matrix[list_holder][placeholder])
            else:
                break
    return sum(list_to_sum)