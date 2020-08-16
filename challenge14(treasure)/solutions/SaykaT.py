def solution(v1,w1,v2,w2,m):
 a=0
 i=[[v1,w1],[v2,w2]]
 i.sort(reverse=True)
 if i[0][1]<=m:
  m-=i[0][1]
  a+=i[0][0]
 if i[1][1]<=m:a += i[1][0]
 return a