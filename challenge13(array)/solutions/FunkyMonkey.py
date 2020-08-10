def solution(a):
 c=0;p,*a=a
 for x in a:
  while x<=p:x+=1;c+=1
  p=x
 return c