def solution(n, l):
    p = []
    for i in range(2, n+1):
        c = True
        for j in range(2, int(i**0.5+1)):
            if not i%j:
                c = False
                break
        if c:
            p.append(i)

    q = dict()
    s = None
    for i in p:
        for j in p:
            if i*j in l:
                q[i*j] = [i, j]
                if s is None:
                    s = min(i,j)

    primes = []
    freq = 0
    for i in range(s, n+1):
        c = True
        for j in range(2, int(i**0.5+1)):
            if not i%j:
                c = False
                break
        if c:
            freq += 1
            primes.append(i)
        if freq == 26:
            break

    m = dict(zip(primes,[chr(i) for i in range(65, 91)]))

    str = ''
    l = [q[i].copy()for i in l]
    s = 0
    ult_c = False
    c = True
    while c:
        c = False
        for i in range(s, len(l)-1):
            if i == s:
                if l[i][0] in l[i+1] and l[i][1] in l[i+1]:
                    c = True
                    ult_c = True
                    s += 1
                    break

                for j in range(2):
                    if l[i][j] not in l[i+1]:
                        str += m[l[i][j]]
                        l[i].remove(l[i][j])
                        break
            str += m[l[i][0]]
            l[i+1].remove(l[i][0])
            if i == len(l)-2:
                str += m[l[i+1][0]]
    if ult_c:
        for i in range(len(l)-1, 0, -1):
            if len(l[i-1]) == 1:
                continue
            else:
                str = m[l[i][0]]+str
                l[i-1].remove(l[i][0])
    return str