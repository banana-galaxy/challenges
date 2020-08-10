def solution(a):
    v = 0
    for i in range(len(a)-1):
        if a[i]>=a[i+1]:
            d=a[i]-a[i+1]+1
            a[i+1]+=d
            v+=d
    return v