def solution(p,q,n):
    if n==0:
        return p==q
    p = ["abcdefgh".index(p[0]),int(p[1])-1]
    q = ["abcdefgh".index(q[0]),int(q[1])-1]
    if (p[0]+p[1]+q[0]+q[1])%2==0:
        if n>1:
            return True
        return abs(p[0]-q[0])==abs(p[1]-q[1])
    return False