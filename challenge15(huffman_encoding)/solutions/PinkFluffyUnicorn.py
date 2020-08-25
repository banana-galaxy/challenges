def solution(a):
 b=a.split()
 for c,(d,e)in enumerate({k:v for k,v in sorted({i:b.count(i)for i in b}.items(),key=lambda f:f[1],reverse=True)}.items()):
  b=[str(c+1)if x==d else x for x in b]
 return ' '.join(b)