def solution(n):
 n=n**(1/2)
 if not n.is_integer():return 0
 if 1<n<4:return 1
 if 2<n:
  for i in range(2,int(n**(1/2)+1)):
   if n%i==0:return 0
  return 1
 return 0