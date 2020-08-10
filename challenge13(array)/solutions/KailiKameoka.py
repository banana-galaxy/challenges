def solution (list):
    moves = 0
    last = list[0]
    for i in range(1, len(list)):
        while (last >= list[i]):
            list[i] = list[i] + 1
            moves = moves + 1
        last = list[i]
    return moves