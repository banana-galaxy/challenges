def matrixSum(matrix:list=[[]]):
    #I was too lazy to make it shorter
    price, cols = 0, list(zip(*matrix))
    for r in cols:
        for p in r:
            if p != 0: price += p
            else: break
    return price