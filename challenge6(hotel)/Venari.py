def matrixSum(rows):
    if not all([all([type(element) == int or type(element) == float for element in row]) for row in rows]):
        raise TypeError("Elements of matrix should all be floats and/or integers")
    upstairs = rows[0]
    total = sum(upstairs)
    for index, row in enumerate(rows):
        if index == 0: continue
        for i, val in enumerate(upstairs):
            if not val:
                row[i] = 0
        total += sum([row[i] for i in range(len(row)) if upstairs[i]])
        upstairs = row
    return total