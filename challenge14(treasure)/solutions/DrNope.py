def solution(val1, w1, val2, w2, wmax):
    valmax = 0
    if w1 + w2 > wmax:
        if w1 <= wmax and w2 <= wmax:
            if val1 > val2:
                valmax = val1
            else:
                valmax = val2
        elif w1 <= wmax or w2 <= wmax:
            if w1 <= wmax:
                valmax = val1
            elif w2 <= wmax:
                valmax = val2
        else:
            valmax = 0
    else:
        valmax = val1 + val2
    return valmax