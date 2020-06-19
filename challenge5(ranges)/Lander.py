def erange(a, b):
    i = a
    l = []
    while 1:
        if i != b:
            l.append(i)
        else:
            break
        i += 1
    return l

def numerate(l, s=0):
    ol = []
    i = s
    for a in l:
        ol.append((i, a))
        i += 1
    return ol