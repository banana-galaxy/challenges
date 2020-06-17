def matrixSum(matrix):
    try:
        nRows, nCols, total = len(matrix), len(matrix[0]), 0  # initial assignments
        ghostedColums = []  # List of columns containing 0s
        for col in range(nCols):  # each column
            for row in range(nRows):  # each row
                if matrix[row][col] == 0:
                    ghostedColums.append(col)  # the whole column is now ghosted
                elif col not in ghostedColums:
                    total += matrix[row][col]  # Add the current value to the sum
        return total
    except TypeError:  # len(matrix[0]) generates a TypeError with one dimension matrix
        return sum(matrix)  # built-in sum function