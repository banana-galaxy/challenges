def solution(v, w, V, W, M):
    if w + W <= M:
        return v + V
    if w <= M >= W:
        if v > V:
            return v
        else:
            return V
    if w <= M <= W:
        return v
    if W <= M <= w:
        return V
    else:
        return 0