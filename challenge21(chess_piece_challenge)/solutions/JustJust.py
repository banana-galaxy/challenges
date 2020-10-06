def solution(a, b, m):
    p = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    d, e, f, g = p[a[0]], int(a[1]), p[b[0]], int(b[1])
    i = min(d + e - f - g, d - e - f + g, key=abs)
    return (i % 2) != 1 and ((i == 0 and m > 0) or m > 1 or a == b)