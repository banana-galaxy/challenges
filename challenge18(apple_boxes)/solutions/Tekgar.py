def solution(n):
    y, r = 0, 0
    for i in range(n + 1):
        if i % 2 == 0:
            r += i * i
        else:
            y += i * i
    return r - y