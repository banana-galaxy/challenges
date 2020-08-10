def solution(inputArray):
    turns = 0
    for index in range(1,len(inputArray)):
        if inputArray[index] <= inputArray[index-1]:
            turns += abs(inputArray[index] - inputArray[index-1]) + 1
            inputArray[index] += turns
    return turns