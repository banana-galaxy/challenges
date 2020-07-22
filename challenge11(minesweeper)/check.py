def solution(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            count = 0
            if matrix[y][x] == 'x':
                continue
            for yi in range(-1,2):
                for xi in range(-1,2):
                    if y+yi >= 0 and x+xi >= 0:
                        if y+yi < len(matrix) and x+xi < len(matrix[y]):
                            if matrix[y+yi][x+xi] == 'x':
                                count += 1
            matrix[y][x] = count
    return(matrix)

if __name__ == '__main__':
    print(solution([[],[],[]]))