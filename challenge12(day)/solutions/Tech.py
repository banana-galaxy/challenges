def calD(d):
    while d > 7:d -= 7
    while d < 1:d += 7
    return d
def solution(day, d1, d2):
    dayNum = ["mo", "tu", "we", "th", "fr", "sa", "su"]
    numDay = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",]
    d1M, d2M = int(d1.split("/")[1]), int(d2.split("/")[1])
    d1N, d2N = ((d1M - 1) * 30 + int(d1.split("/")[0]),(d2M - 1) * 30 + int(d2.split("/")[0]),)
    day, d3 = dayNum.index(day[:2].lower()) + 1, calD(abs(d2N - d1N))
    checkI = lambda m1, m2, n1, n2: (n2, n1) if m1 > m2 or n1 > n2 else (n1, n2)
    final = (lambda n1, n2, d, m1, m2: numDay[(calD(n2 - n1 + d) - 1)]if m2 > m1 else numDay[(calD(d - (n2 - n1)) - 1)])
    d1N, d2N = checkI(d1M, d2M, d1N, d2N)
    d3 = final(d1N, d2N, day, d1M, d2M)
    return d3