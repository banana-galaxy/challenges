def solution(v1, w1, v2, w2, maxW):
    if w1 + w2 <= maxW: return v1 + v2
    if w1 <= maxW and w2 <= maxW:
        return v1 if v1 > v2 else v2
    if w1 <= maxW: return v1
    if w2 <= maxW: return v2
    return 0