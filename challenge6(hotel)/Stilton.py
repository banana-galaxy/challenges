def matrixSum(matrix):
    ghost_column = []
    result = 0
    column_index = 0
    for line in matrix:
        for column in line:
            if column_index not in ghost_column:
                if column == 0:
                    ghost_column.append(column_index)
                else:
                    result += column
            column_index += 1
        column_index = 0
    return result