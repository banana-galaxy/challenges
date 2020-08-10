def solution(inputArray):
    count = 0
    for idx, val in enumerate(inputArray):
        if idx != 0:
            while inputArray[idx] <= inputArray[idx - 1]:
                count += 1
                inputArray[idx] += 1
    return count