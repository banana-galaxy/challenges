def matrixSum(mat):
    unpackt = []
    dimy, dimx = len(mat), len(mat[0])
    unpackt.extend([y for x in mat for y in x])

    count = 0
    for i in range(dimx):
        for j in range(dimy):
            if unpackt[i+j*dimx] == 0:
                break
            else:
                count += unpackt[i+j*dimx]
    return count