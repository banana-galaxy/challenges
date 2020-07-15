def fill(chessboard):
    for number, line in enumerate(chessboard):
        for index, square in enumerate(line):
            if square == 0:
                if len(line) > index + 1 and line[index + 1] == 0:
                    chessboard[number].pop(index)
                    chessboard[number].insert(index, 1)
                    chessboard[number].pop(index + 1)
                    chessboard[number].insert(index + 1, 1)

                elif len(chessboard) > number + 1 and chessboard[number + 1][index] == 0:
                    chessboard[number].pop(index)
                    chessboard[number].insert(index, 1)
                    chessboard[number + 1].pop(index)
                    chessboard[number + 1].insert(index, 1)

    for line in chessboard:
        if 0 in line:
            return False
    return True