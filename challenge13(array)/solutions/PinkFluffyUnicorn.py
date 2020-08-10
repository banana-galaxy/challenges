def solution(l):
    i,j=0,0
    while len(l)>j:
        if len(l)!=j+1:
            f,s=l[j],l[j+1]
            if f>=s:
                l[j+1]+=1;i+=1;j-=1
        j+=1
    return i