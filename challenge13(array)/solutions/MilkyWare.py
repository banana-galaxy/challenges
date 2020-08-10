def solution(inputArray, count=0, i=0):
    while i in range(len(inputArray) - 1):
        if inputArray[i] < inputArray[i + 1]:
            i += 1
        else:
            inputArray[i + 1] += 1
            count += 1
    print(count)
