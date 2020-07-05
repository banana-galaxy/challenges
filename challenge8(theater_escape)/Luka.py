def whichExit(matrix):
    for something, row in enumerate(matrix):
        if 0 in row:
            index = something, row.index(0)
    row = matrix[index[0]]
    erase = []
    for e, i in enumerate(row):
        if i == -1:
            erase.append(e)
    for i in reversed(erase):
        row.pop(i)

    chosenone = row.index(0)
    print(chosenone)
    left = -1
    right = -1
    while chosenone > -1:
        left += 1
        chosenone -= 1

    chosenone = row.index(0)
    print(chosenone)
    while chosenone < len(row):
        right += 1
        chosenone += 1

    print(row, right, left)
    if right > left:
        return "left"
    elif right < left:
        return "right"
    else:
        return "same"