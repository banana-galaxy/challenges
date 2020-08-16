def solution(a,b,c,d,e):
  if b+d<=e: return a+c
  if b>e and d>e:return 0
  v=c if d<=e else a
  if a>=c:
    v=a if b<=e else c
  return v