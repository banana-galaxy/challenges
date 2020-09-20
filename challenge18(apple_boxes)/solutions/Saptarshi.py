def solution(k:int)->int:
    m=n=0
    for i in range(1,k+1):
        if i%2==0:n+=i*i
        else:m+=i*i
    return n-m