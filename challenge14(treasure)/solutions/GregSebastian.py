def solution(v1, w1, v2, w2, mw):
    vbd1, vbd2 = v1/w1, v2/w2
    if (w1 >= mw) and (w2 >= mw):
        return 0
    else:
        if (w1+w2) <= mw:
            return v1+v2
        elif (vbd1 < vbd2):
            return v2
        elif (vbd1 > vbd2):
            return v1