def fill(matrix):
    def zeros(matrix):
        r = 0
        for i in matrix:
            r+=i.count(0)
        return r
    x={}
    if zeros(matrix)%2==1:
        return False
    def empty_around(matrix, i, j):
        k=0
        empty=[]
        if  0<= i-1<=len(matrix)-1 and matrix[i-1][j]==0:
            k+=1
            empty.append((i-1,j))
        if  0<= i+1<=len(matrix)-1 and matrix[i+1][j]==0:
            k+=1
            empty.append((i+1,j))
        if  0<= j-1<=len(matrix[i])-1 and matrix[i][j-1]==0:
            k+=1
            empty.append((i,j-1))
        if  0<= j+1<=len(matrix[i])-1 and matrix[i][j+1]==0:
            k+=1
            empty.append((i,j+1))
        return k, empty
    def check(matrix):
        x = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    continue
                k, _=empty_around(matrix, i, j)
                if k == 0:
                    return False
                if k in x:
                    x[k].append((i,j))
                else:
                    x[k]=[(i,j)]
        if 1 not in x:
            return True
        for dane in x[1]:
            k, empty= empty_around(matrix, j, i)
            if k == 0:
                return False
            for empt in empty:
                matrix[empt[0]][empt[1]] = 1
    while zeros(matrix) != 0:
         answ = check(matrix)
         if answ!=None:
             return answ
    return True