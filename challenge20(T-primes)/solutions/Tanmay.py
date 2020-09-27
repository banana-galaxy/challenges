def solution(x):
 n=x**.5
 if n!=1 and round(n)==n:
  if n==2:
   return 1
  if n%2==0:
   return 0
  d=int(n**.5)
  for i in range(3,d+1,2):
   if n%i==0:
    return 0
  return 1
 else:
  return 0