def solution(_,a):
 k=len(a)
 gcd=lambda a,b:gcd(b,a%b) if b != 0 else a
 b=[0]*(k+1)
 for i in range(k):
  o=gcd(a[i],a[i+1])
  if o!=a[i]:
   b[i+1]=o
   for j in range(i+2,k+1):b[j]=a[j-1]//b[j-1]
   for j in range(i,-1,-1):b[j]=a[j]//b[j+1]
   break
 v=sorted(set(b))
 return''.join(chr(65+v.index(x))for x in b)