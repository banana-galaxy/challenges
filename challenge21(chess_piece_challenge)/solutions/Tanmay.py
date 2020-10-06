def solution(x,y,n):
 if n==0:
  return x==y
 a=list("abcdefgh")
 i,j=a.index(x[0]),a.index(y[0])
 p=sorted([i%2, int(x[1])%2])
 q=sorted([j%2, int(y[1])%2])
 if p==q or 1==len(set(p))==len(set(q)):
  if n>=2:
   return 1
  return abs(i-j)==abs(int(x[1])-int(y[1]))
 return 0