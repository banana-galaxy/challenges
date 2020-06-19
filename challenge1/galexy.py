def solution(matrix, end=64):
    start = len(matrix)
    diff = int(end / start)
    result = []

    for x in range(start):
        for xi in range(diff):
            result.append([])
            latest_x = len(result)-1

            for y in range(len(matrix[x])):
                for yi in range(diff):
                    result[latest_x].append(matrix[x][y])  

    return result