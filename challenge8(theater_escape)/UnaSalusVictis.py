def whichExit(matrix):
    for row in matrix:
        if 0 in row:
            left = sum([x for x in row[:row.index(0)] if x == 1])
            right = sum([x for x in row[row.index(0):] if x == 1])

            return "same" if left == right else "left" if left < right else "right"