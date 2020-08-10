def solution(inputArray):
    moves = 0
    for x in range(1, len(inputArray)):
        if inputArray[x] <= inputArray[x - 1]:
            moves += 1 + (inputArray[x - 1] - inputArray[x])
            inputArray[x] += 1 + (inputArray[x - 1] - inputArray[x])

    return moves