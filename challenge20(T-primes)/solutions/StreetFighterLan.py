def solution(n):
    pct = 0
    for x in range(1, int(n)+1):
        if int(n) % x == 0:
            pct += 1
    if pct == 3:
        return True
    return False