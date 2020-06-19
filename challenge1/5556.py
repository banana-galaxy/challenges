def solution(matrix):
    matrix_size = len(matrix)
    new_matrix = [[] for counter in range(64)]
    size_of_pixel = int(64 / matrix_size)
    row_no = 0
    for row in matrix:
        offset = row_no * size_of_pixel
        for pixel in row:
            for col in range(size_of_pixel):
                for counter in range(size_of_pixel):
                    new_matrix[col + offset].append(pixel)
        row_no += 1