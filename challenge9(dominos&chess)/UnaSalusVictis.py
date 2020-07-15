def fill(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    odds = 0
    evens = 0
    cur_bool = True
    row_start = True
    for row in range(rows):
        cur_bool = row_start
        for col in range(cols):
            if cur_bool and not matrix[row][col]: odds += 1
            elif not matrix[row][col]: evens += 1

            cur_bool = False if cur_bool else True

        row_start = False if row_start else True

    if odds != evens: return False

    def surrounding(row, col):
        out = []
        for i in [-1, 1]:
            if row + i >= 0 and row + i < rows:
                out.append((row + i, col))

            if col + i >= 0 and col + i < cols:
                out.append((row, col + i))

        return out

    def has_neighbors(row, col):
        neighbors = surrounding(row, col)
        for neigh in neighbors:
            if matrix[neigh[0]][neigh[1]] == 0:
                return True

        return False

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0 and not has_neighbors(row, col):
                return False

    def is_solved():
        for row in matrix:
            if 0 in row: return False

        return True

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                neighbors = surrounding(row, col)
                for neigh in neighbors:
                    val = matrix[neigh[0]][neigh[1]]
                    if val == 0:
                        matrix[row][col] = 1
                        matrix[neigh[0]][neigh[1]] = 1

                        if is_solved(): return True

                        if fill(matrix): return True

                        matrix[row][col] = 0
                        matrix[neigh[0]][neigh[1]] = 0

    return False