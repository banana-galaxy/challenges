def solution(v1, w1, v2, w2, mw):
    v={w1:v1,w2:v2}
    w={v1:w1,v2:w2}
    x,y = 0,0
    if x+w[max(v1, v2)]<=mw and min(v1, v2) != max(v1, v2):
        x += w[max(v1, v2)]
        y += max(v1, v2)
    if x+w[min(v1,v2)]<=mw and min(v1, v2) != max(v1, v2):
        x += w[min(v1,v2)]
        y+=min(v1, v2)
    elif min(v1, v2) == max(v1, v2):
        if x+min(w1, w2)<=mw:
            x += min(w1, w2)
            y += v[min(w1, w2)]
        if x+max(w1, w2)<=mw:
            x += max(w1, w2)
            y += v[max(w1, w2)]
    return y