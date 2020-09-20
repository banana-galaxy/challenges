def solution(x):
    if x%2==0:
        e=x/2
        o=x/2
        e=2*e*(e+1)*(2*e+1)/3
        o=o*(2*o+1)*(2*o-1)/3
        return int(e-o)
    else:
        e=x//2
        o=x//2+1
        e=2*e*(e+1)*(2*e+1)/3
        o=o*(2*o+1)*(2*o-1)/3
        return int(e-o)