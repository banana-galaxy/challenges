def solution(list):
    cnt = 0
    for i, j in enumerate(list[1:]):
        if j <= list[i-1]:
            cnt += list[i-1] - j + 1
            list[i] = list[i-1] + 1
    return cnt