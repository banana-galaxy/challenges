def solution(x):
    s=0
    if x:
        p,*x=x
        for c in x:
            if c<=p: p+=1;s+=p-c
            else: p=c
    return s