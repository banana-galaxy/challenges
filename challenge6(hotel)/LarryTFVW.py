def matrixSum(matrix):
    total = 0.00
    badnum = []
    for m in matrix:
        goodnum = list(range(len(m)))
        for a in range(0,len(m)):
            if m[a] == 0 or m[a] == 0.00:
                if not a in badnum:
                    goodnum.remove(a)
                    badnum.append(a)
            else:
                if not a in badnum:
                    total += m[a]
    return total