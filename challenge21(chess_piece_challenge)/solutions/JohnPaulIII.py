def solution(s, e, m):
    if m < 1:
        return s == e
    s0, s1, e0, e1 = (ord(s[0]) - 64) % 32, int(s[1]), (ord(e[0]) - 64) % 32, int(e[1])
    if (s0 + s1) % 2 == (e0 + e1) % 2:
        if m > 1:
            return 1
        return abs(s0 - e0) == abs(s1 - e1)
    return 0