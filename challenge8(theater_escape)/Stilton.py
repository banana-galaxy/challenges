def whichExit(matrix):
    for line in matrix:
        if 0 in line:
            chair = [matrix.index(line), line.index(0)]

    right, left = 0, 0

    for place in matrix[chair[0]][chair[1]+1:]:
        if place == 1:
            right += place
    for place in matrix[chair[0]][0:chair[1]]:
        if place == 1:
            left += place

    if left < right:
        return "left"
    elif left > right:
        return "right"
    else:
        return "same"