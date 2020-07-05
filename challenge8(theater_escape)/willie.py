def whichExit(matrix):
    for row in matrix:
        if 0 not in row:
            continue

        i = row.index(0)
        l_sum = row[:i].count(1)
        r_sum = row[i + 1:].count(1)

        if l_sum == r_sum:
            return "same"
        elif l_sum < r_sum:
            return "left"
        else:
            return "right"