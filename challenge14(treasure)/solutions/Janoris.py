def solution(v1, w1, v2, w2, mw):
    running_value = running_weight = 0

    if v1 > v2:
        if w1 <= mw:
            running_value += v1
            running_weight += w1

    if w2 <= mw - running_weight:
        running_value += v2
        running_weight += w2

    return running_value