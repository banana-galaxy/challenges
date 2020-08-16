def solution(a,b,c,d,m):
 if b+d<=m:return a+c
 if b<=m:return c if d<=m and a<=c else a
 return c if d<=m else 0