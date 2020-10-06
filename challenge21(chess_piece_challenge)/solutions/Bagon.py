def solution(a,b,n):
 z='abcdefgh'
 x1,y1,x2,y2=int(a[1])-1,z.index(a[0]),int(b[1])-1,z.index(b[0])
 if abs(x1-x2)==abs(y1-y2):
  return n>0 or a==b
 if(x1+y1)%2!=(x2+y2)%2 or n<1:
  return a==b
 return n>1