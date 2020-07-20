def lateRider(n):
    sum= 0
    nearDivide = n//60
    reaminder = n%60
    # print(nearDivide, reaminder)
    nD = str(nearDivide)
    r = str(reaminder)
    # print(nD, r)
    for i in range(len(nD)):
        sum += int(nD[i])
    # print(sum)
    for j in range(len(r)):
        sum += int(r[j])
    return sum