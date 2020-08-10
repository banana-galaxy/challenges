def solution(array) -> int:
    steps = 0
    for i in range(len(array)-1):
        while array[i] >= array[i+1]:
            array[i+1] += 1
            steps += 1
    return steps