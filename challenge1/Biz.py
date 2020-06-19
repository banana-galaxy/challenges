def solution(matrix, out=64):
    return [[matrix[i//int(out / len(matrix))][n//int(out / len(matrix))] for n in range(out)] for i in range(out)]