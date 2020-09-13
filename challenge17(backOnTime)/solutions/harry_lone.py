def solution(L):
    x = 0, y = 0
    d = {“n”: [0,1],”s”:[0,-1],”e”:[1,0],”w”[-1,0]}
    if len(L) > 10:
        return False
    for v in L:
            x += d[v][0]
            y += d[v][1]
    if x == 0 and y == 0:
        return True
    else:
        return False 