def solution(m,n=64): #scales the matrix up!
    new = []
    inner = []
    data = enumerate(m)
    for i in data:
        for x in range(0,n):
            for d in i[1]:
                #print(round(int(n/2)))
                for x in range(0,round(int(n/2))):
                                    for x in range(0,round(int(n/2))):
                                        inner.append(d)
            new.append(inner)
            inner = []

    return new
def matrixfromnum(num:int):
    new = []
    inner = []
    for x in range(0,num):
        for z in range(1,num + 1):
            inner.append(z)
        new.append(inner)
        inner = []
    return new
def formatmatrix(m):
    strs = '['
    x = 0
    full = len(m)
    for data in m:
        x += 1
        if x >= full:
            strs += str(data) + ']'
        else:
            strs += str(data) + ',\n'
    return strs
if __name__ == "__main__":
    f = [[1,2,3,4], #the matrix to scale
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
    print(formatmatrix(matrix(f,4))) #SCALE THE MATRIX TO 16X16 from factors 