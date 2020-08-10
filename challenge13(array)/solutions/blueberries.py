def solution(l):
    c=n=1
    while n:
        n=0
        for i in range(len(l)-1):
            if l[i]>=l[i+1]:
                l[i+1]+=1
                n=1
                c+=1
    return c-1