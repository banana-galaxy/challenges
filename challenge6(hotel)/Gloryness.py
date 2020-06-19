stop = 1
class MatrixError(Exception):
    def __init__(self, reason=""):
        MatrixError.__module__ = 'matrix'
        global stop
        if stop == 1: # to avoid recursion
            stop = 2
            raise MatrixError(reason)
        else:
            pass

def matrixSum(matrix):
    all_in_one = []
    amount_each_line = []

    for i in range(len(matrix)):
        amount_each_line.append(len(matrix[i]))

    req = len(matrix[0])

    # some list comprehension
    is_same = [1 if i == req else 0 for i in amount_each_line]
    [MatrixError("All lists must be same length within the matrix.") if i == 0 else None for i in is_same]

    for num in matrix:
        all_in_one.extend(num)

    result = []
    amount = amount_each_line[0]

    for index, num in enumerate(all_in_one):
        if num == 0:
            pass
        else:
            if index >= amount:
                if all_in_one[index-amount] == 0:
                    pass
                elif all_in_one[index-amount] != 0:
                    result.append(num)
            elif index < amount:
                if all_in_one[index+amount] != 0:
                    result.append(num)

                elif all_in_one[index+amount] == 0:
                    result.append(num)
    return sum(result)