def matrixSum(m):
    global prev
    prev = []
    sum = 0
    for i in range(len(m)):
        if i == 0:
            for j in range(len(m[i])):
                sum += m[i][j]
        else:
            for k in range(len(m[i])):
                if prev[k] != 0:
                    sum += m[i][k]
                elif prev[k] == 0:
                    for l in range(len(m)):
                        m[l][k] = 0
        prev = m[i]
    return sum