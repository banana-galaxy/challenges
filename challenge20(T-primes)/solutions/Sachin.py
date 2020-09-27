def solution(n):
 n=n**.5
 if n!=n//1:return False
 if n<=3:return n>1
 elif n%2==0 or n%3==0:return False
 i=5
 while i*i<=n:
  if n%i==0 or n%(i+2)==0:return False
  i += 6
 return True 