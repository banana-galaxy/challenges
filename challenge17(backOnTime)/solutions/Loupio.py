def solution(p):
    return all([p.count(a) == p.count(b) for a, b in ("ns", "ew")] + [len(p) <= 10])