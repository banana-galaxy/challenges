def solution(k):
    if k % 2 == 0:
        return k * (k+1) // 2
    else:
        return - k * (k+1) // 2