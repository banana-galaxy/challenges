def solution(l):
    c=0
    for i in range(len(l)-1):
        while l[i]>=l[i+1]:
            l[i+1]+=1
            c+=1
    return c