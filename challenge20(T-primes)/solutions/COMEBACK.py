def solution(x):
    if x<2 or x%2<1:return x==4
    a=int(x**0.5);b=int(a**0.5)
    if a**2!=x:return 0
    for i in range((b-1)//2+1):
        if a%(2+i)<1 or a%(b+1-i)<1:return 0
    return 1