def matrixSum(matrix):
    bad_numbers = []
    sum = 0
    for row in matrix:
        counter = 0
        for number in row:
            counter += 1
            if counter in bad_numbers:
                continue
            else:
                sum += number
            if number == 0:
                bad_numbers.append(counter)
    return sum