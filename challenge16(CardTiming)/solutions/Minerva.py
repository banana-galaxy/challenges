def solution(d):
    r = [31] if d == 28 else None
    r2 = [31] if d == 30 else [28, 30, 31]
    return r if r else r2