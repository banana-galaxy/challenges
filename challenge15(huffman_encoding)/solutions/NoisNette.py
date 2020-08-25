def solution(s):
    wr=s.split()
    c={w:wr.count(w)for w in wr}
    ws=[w for w in sorted(c,key=c.get,reverse=True)]
    return ' '.join(str(ws.index(w) + 1) for w in wr)