g=lambda n,m:g(m,n%m)if m else n
def solution(_,e):
 k=-~len(e)
 b=[1]*k
 for i in range(k-2):
  c=g(e[i],e[-~i])
  if c==e[i]:continue
  b[-~i]=c
  for w in range(i+2,k):b[w]=e[~-w]//b[~-w]
  for w in range(i,-1,-1):b[w]=e[w]//b[-~w]
 return"".join(chr(65+[*sorted(set(b))].index(l))for l in b)