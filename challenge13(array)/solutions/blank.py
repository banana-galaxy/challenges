def solution(inputArray):
    moveCount = 0
    while True:
        flag = False
        for i in range(len(inputArray)-1):
            if not(inputArray[i] < inputArray[i+1]):
                inputArray[i+1] += 1
                moveCount += 1

        for i in range(len(inputArray)-1):
            if inputArray[i] > inputArray[i+1] or inputArray[i] == inputArray[i+1]:
                flag = True

        if not flag:
            break

    return moveCount