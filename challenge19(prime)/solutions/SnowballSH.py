g=lambda a,b:g(b,a%b)if b else a
def solution(_,a):
 k=len(a)+1
 b=[-1]*(k)
 for i in range(k-2):
  o=g(a[i],a[i+1])
  if o!=a[i]:
   b[i+1]=o
   for w in range(i+2,k):b[w]=a[w-1]//b[w-1]
   for w in range(i,-1,-1):b[w]=a[w]//b[w+1]
 return "".join(chr(65+[*sorted(set(b))].index(v))for v in b)