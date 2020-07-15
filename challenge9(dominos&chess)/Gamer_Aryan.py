def fill(mat):
    possible = True
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if j < len(mat[i])-1:
                if mat[i][j] == 0 and mat[i][j+1] == 0:
                    mat[i][j] = 1
                    mat[i][j+1] = 1
            if i < len(mat)-1:
                if mat[i][j] == 0 and mat[i+1][j] == 0:
                    mat[i][j] = 1
                    mat[i+1][j] = 1
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                possible = False
    return possible