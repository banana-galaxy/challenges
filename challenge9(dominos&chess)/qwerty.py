def fill(matrix):
    open = 0
    for row in matrix:
        for col in row:
            if col == 0:
                open += 1

    if open%2==0:
        return True
    else:
        return False