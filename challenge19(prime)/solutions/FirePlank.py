def solution(k,l):
  z=len(l)
  p=[0for _ in range(z+1)]
  g=lambda a,b:a if b==0else g(b,a%b)
  for i in range(z):
    t=g(l[i],l[i+1])
    if t!=l[i]:
      p[i+1]=t
      for x in range(i+2, z+1):p[x]=l[x-1]/p[x-1]
      for y in range(i,-1,-1):p[y]=l[y]/p[y+1]
      break
  a=sorted(set(p))
  s=""
  for i in p:s+=chr(65+(a.index(i)))
  return s