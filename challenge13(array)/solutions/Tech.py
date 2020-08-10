def solution(a):
    if len(a) > 0: p = a[0]
    m = 0
    c = lambda x: (p - a[i]) + 1 if a[i] <= p else x
    for i in range(1, len(a)):
        m += c(m)
        a[i] += c(a[i])
        p = a[i]
    return m