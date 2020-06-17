def matrixSum(l):
    return sum(l[0])+sum(sum(map(lambda x: (x[1] if x[0]>0 else 0),zip(x, x[1:]))) for x in zip(*l))