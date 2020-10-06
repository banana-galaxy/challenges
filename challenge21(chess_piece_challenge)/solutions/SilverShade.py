def solution(a, b, n):
    a,b=a.lower(),b.lower()
    if n < 1 and a!=b:return False
    if a==b:return True
    r = [[f'{l}{n}' for n in range(1, 9)] for l in 'abcdefgh']
    bl, i = {}, 0
    for x in r:
        c = i
        for f in x:
            c = not c
            bl[f] = c
        i = not c
    if bl[a] == bl[b]:
        if n < 2:
            i = [[g.index(a), f] for f, g in enumerate(r) if a in g][0]
            m = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
            j = []
            for l in m:
                k = i.copy()
                for x in range(9):
                    try: j.append(r[k[1]][k[0]])
                    except: pass
                    k[0] += l[0]
                    k[1] += l[1]
                    if any(x < 0 for x in k):
                        break
            if b in j: return True
            else: return False
        else: return True
    else: return False