def whichExit(cinema):
    currentRow, currentColumn, left, right, i = 0, 0, 0, 0, 0
    for row in cinema:
        for sit in row:
            if sit == 0: currentRow = row.index(sit); currentColumn = cinema.index(row)
    for column in range(currentColumn + 1):
        for _ in cinema[column]:
            if i < currentRow:
                left += 0 if cinema[column][i] == -1 else 1
            elif i == currentRow: i += 1; continue
            else: right += 0 if cinema[column][i] == -1 else 1
            i += 1
        i = 0
    if left == right: return "same"
    elif left > right: return "right"
    else: return "left"