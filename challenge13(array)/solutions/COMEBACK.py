def solution(l):
    m=0
    t=l[0]
    for n in l[1:]:
        if n>t:t=n
        else:t+=1;m+=t-n
    return m