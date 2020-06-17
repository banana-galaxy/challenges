def matrixSum(matrix):
    dropped = set()
    answer = 0
    height, width = len(matrix), len(matrix[0])
    for y in range(height):
        for x in range(width):
            if x not in dropped:
                cell = matrix[y][x]
                if cell == 0:
                    dropped.add(x)
                else:
                    answer += cell
    return answer