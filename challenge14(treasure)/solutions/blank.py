def solution(v, w, V, W, m):
    wc, vc = 0, 0
    if w + W <= m:
        return v + V
    else:
        if w <= m:
            vc += v
            wc += w
        if m - wc >= W:
            vc += V
    return vc