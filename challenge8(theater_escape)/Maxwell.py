def whichExit(matrix):
    for row in matrix:
        if 0 in row:
            left_people = sum([x for x in row[:row.index(0)] if x == 1])
            right_people = sum([x for x in row[row.index(0):] if x == 1])
            return("left" if left_people < right_people else "right" if right_people < left_people else "same")