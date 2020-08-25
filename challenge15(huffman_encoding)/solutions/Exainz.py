def solution(s):
    t = s.split()
    d = {}
    n = {}
    x = 1
    r = ""
    for i in t:
        d[i] = t.count(i)
    for h in sorted(d.items(), key=lambda x:x[1], reverse=True):
        n[h[0]] = h[1]
    for k,v in n.items():
        n[k] = x
        x += 1
    for j in t:
        r += str(n[j]) + " "
    return r[:-1]