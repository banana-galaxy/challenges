def solution(a,b,n):
    if n==0:return a==b
    x,y=abs(ord(a[0])-ord(b[0])),abs(int(a[1])-int(b[1]))
    if n==1:return x==y
    return x%2==y%2