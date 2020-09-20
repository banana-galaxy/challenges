def solution(k):
    n_red, n_yellow = 0, 0
    for i in range(k+1):
        if i % 2 == 0:
            n_red += i*i
        else:
            n_yellow += i*i
    return n_red - n_yellow