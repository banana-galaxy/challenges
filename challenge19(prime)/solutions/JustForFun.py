def solution(_,a):
 g=lambda a,b:g(b,a%b)if b else a
 z=len(a);b=[0]*(z+1)
 for i in range(z):
  if g(a[i],a[i+1])!=a[i]:
   b[i+1]=g(a[i],a[i+1])
   for m in range(i+2,z+1):b[m]=a[m-1]/b[m-1]
   for m in range(i,-1,-1):b[m]=a[m]/b[m+1]
   break
 l=sorted(set(b))
 return''.join(chr(65+l.index(h))for h in b)