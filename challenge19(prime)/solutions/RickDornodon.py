def solution(a,b):
  for v in range(int(b[0]**.5),1,-1):
    if b[0]%v==0:f=[v,b[0]//v];break
  u=[]
  for p in (f,f[::-1]):
    u.extend(p)
    for v in b[1:]:
      c,d=divmod(v,u[-1])
      if d:break
      else:u.append(c)
    if len(u)==len(b)+1:break
    else:u.clear()
  return''.join(map({p:chr(65+i)for i,p in enumerate(sorted({*u}))}.get,u))