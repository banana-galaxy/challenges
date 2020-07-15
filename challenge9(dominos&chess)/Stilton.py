def fill(matrix):
    missing = []
    for index, row in enumerate(matrix, 1):
        for indexs, square in enumerate(row, 1):
            if square == 1:
                missing.append((index, indexs))

    if ((len(matrix) * len(matrix[0]) - len(missing)) % 2) != 0:
        return False

    if ((len(matrix) * len(matrix[0])) % 2) != 0:
        white, black = (len(matrix) * len(matrix[0])) / 2, ((len(matrix) * len(matrix[0])) / 2) + 1

    else:
        white, black = (len(matrix) * len(matrix[0])) / 2, (len(matrix) * len(matrix[0])) / 2

    for square in missing:
        if square[0] % 2 == 0 and square[1] % 2 == 0:
            black -= 1
        elif square[0] % 2 == 0 and square[1] % 2 != 0:
            white -= 1
        elif square[0] % 2 != 0 and square[1] % 2 != 0:
            black -= 1
        else:
            white -= 1

    if black == white:
        return True
    else:
        return False