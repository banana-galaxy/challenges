def solution(s):
    wd, wl = {}, s.split()
    for w in wl:
        wd[w] = wd[w] + 1 if w in wd else 1
    F = {w: f for f, w in enumerate(sorted(wd, key=lambda x: wd[x], reverse=True), 1)}
    return " ".join(str(F[W]) for W in wl)