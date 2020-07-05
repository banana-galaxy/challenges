def whichExit(matrix):
    for row in matrix:
        if 0 in row:
            pos = row.index(0)
            left = 0
            right = 0
            for x in row[:pos]:
                if x == 1:
                    left += 1
            for x in row[pos+1:]:
                if x == 1:
                    right += 1
            break
    if left == right:
        return "same"
    elif left > right:
        return "right"
    else:
        return "left"