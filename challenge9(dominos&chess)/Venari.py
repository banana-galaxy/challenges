def fill(M):
    """
    Checks if permutation of configuration is even compared to trivial solution.
    """
    # Quick check whether the amount of zeros is even.
    zeros = len(M) * len(M[0])
    for r in M:
        zeros -= r.count(1)
    if zeros % 2:
        return False

    # Not so quick check whether any zeros are enclosed.
    nns = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for i in range(len(M)):
        r = M[i]
        if not r.count(1): continue
        for j in range(len(r)):
            pos = [j, i]
            enclosed = 0
            for nn in nns:
                x = pos[0] + nn[0]
                y = pos[1] + nn[1]
                #Check if zeros are enclosed by walls
                if y >= len(M) or y < 0:
                    enclosed += 1
                if x >= len(r) or x < 0:
                    enclosed += 1
                #check if zeros are enclosed by occupied spaces.
                if y < len(M) and y >= 0:
                    if x < len(r) and x >= 0:
                        r = M[y]
                        if r[x]:
                            enclosed += 1
                if enclosed == 4:
                    return False

    p = 0
    c = 0
    lc = 0
    for r in M:
        c += r.count(1)
        if not c % len(r) and c > lc:
            lc = c
            p += 1
        for e in r:
            if e:
                i = r.index(e)
                p += i + M.index(r)
                r[i] = 0
    return (p + c) % 2