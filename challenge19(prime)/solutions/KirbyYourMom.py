def solution(p,v):
 F=lambda v,s:F(s,v%s)if s else v
 l=len(v)+1
 s=[-1]*l
 for i in range(l-2):
  f=F(v[i],v[i+1])
  if f!=v[i]:
   s[i+1]=f
   for j in range(i+2,l):s[j]=v[j-1]//s[j-1]
   for j in range(i,-1,-1):s[j]=v[j]//s[j+1]
 return''.join(chr(sorted(set(s)).index(x)+65)for x in s)