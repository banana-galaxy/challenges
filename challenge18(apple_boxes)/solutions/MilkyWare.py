def solution(k):
    s=S=0
    for i in range(k+1):
        if i%2==0:s+=i*i
        else:S+=i*i
    return s-S