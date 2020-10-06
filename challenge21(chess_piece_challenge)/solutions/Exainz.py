def solution(sp, fp, m):
    if m < 1:
        return sp == fp
    else:
        (s, S) = ord(sp[0]), int(sp[1])
        (e, E) = ord(fp[0]), int(fp[1])
        if m == 1:
            return abs(e - s) == abs(E - S) and ((s + S) % 2 == 0) == ((e + E) % 2 == 0)
        elif m > 1:
            return ((s + S) % 2 == 0) == ((e + E) % 2 == 0)