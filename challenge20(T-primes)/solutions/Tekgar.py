def solution(x):
    return len({f for i in range(1,int(x**.5)+1) if x%i==0 for f in [i,x//i]})==3