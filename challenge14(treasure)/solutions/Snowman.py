def solution(a, b, c, d, e):
    if b + d <= e:
        return a + c
    elif b > e and d > e:
        return 0
    elif b > e and d <= e:
        return c
    elif d > e and b <= e:
        return a
    else:
        return max(a, c)