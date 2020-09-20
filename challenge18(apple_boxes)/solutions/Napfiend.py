def solution(k):
    if k%2:
        e=(k-1)/2
        o=(k+1)/2
    else:
        e=o=k/2
    return int(((2*e)*((2*e*e)+(3*e)+1)/3)-(o*((4*o*o)-1)/3))