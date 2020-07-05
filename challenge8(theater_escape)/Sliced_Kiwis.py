def whichExit(r,c,matrix):
    flag=0
    coord = [0,0]
    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j]==0:
                flag=1
                coord=[i,j]
                break
        if flag:
            break


    sum=0
    sum2=0
    for i in range(coord[1], c):
        sum += matrix[coord[0]][i]

    for i in range(0, coord[1]):
        sum2 += matrix[coord[0]][i]


    if sum==sum2:
        return "same"

    if sum2 > sum:
        return "left"

    return "right"