def solution(k):
    s1=0;s2=0
    for i in range(k+1):
        if i%2 is 0:
            s1+=i*i
        else:
            s2+=i*i
    return s1-s2