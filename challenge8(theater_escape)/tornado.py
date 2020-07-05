def whichExit(m):
    [m] = [m[i] for i in range(len(m)) if 0 in m[i]]
    l = m[:m.index(0)].count(1)
    r = m[m.index(0) + 1:].count(1)
    if l < r:
        return "left"
    elif r < l:
        return "right"
    else:
        return "same"