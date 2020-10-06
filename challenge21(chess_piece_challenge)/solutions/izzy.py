def solution(a, b, k):
    if a == b: 
        return 1
    x, y = (int(i, 35) % 2 for i in (a, b))
    if x == y:
        l = "abcdefgh"
        d = 1 if abs(int(a[1]) - int(b[1])) == abs(l.index(a[0]) - l.index(b[0])) else 2
        return d <= k
    return 0