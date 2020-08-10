def solution(array):
    output = 0
    for i in range(len(array) - 1):
        while array[i] >= array[i + 1]:
            array[i + 1] += 1
            output += 1
    return output