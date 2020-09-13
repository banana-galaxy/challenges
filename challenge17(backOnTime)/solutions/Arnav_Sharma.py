def solution(l):
    if len(l) > 10:
        return False
    v = h = 0
    for i in l:
        if i.lower() == 'n':
            v += 1
        elif i.lower() == 's':
            v -= 1
        elif  i.lower() == 'e':
            h += 1
        else:
            h -= 1
    if  v == h == 0:
        return True
    return False