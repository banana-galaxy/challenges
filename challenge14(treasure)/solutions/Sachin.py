def solution(v1, w1, v2, w2, maxW):
    if w1 + w2 <= maxW:
        return v1 + v2
    elif w1 < w2 <= maxW:
        return v2
    elif w2 < w1 <= maxW:
        return v1
    else:
        return 0