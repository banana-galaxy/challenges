def solution(list):
    times = 0
    for i in range(len(list) - 1):
        if list[i] > list[i + 1] or list[i] == list[i + 1]:
            differ = list[i] - list[i + 1]
            list[i + 1] += differ + 1
            times += differ + 1
    return times