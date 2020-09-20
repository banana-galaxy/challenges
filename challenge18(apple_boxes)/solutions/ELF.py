def solution(k,a=0):
 for i in range(1,k+1):
  if i%2==0:
   a+=i*i
  else:
   a-=i*i
 return a