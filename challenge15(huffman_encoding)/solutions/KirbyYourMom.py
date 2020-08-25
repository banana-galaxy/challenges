def solution(s) -> str:
  s,v,f=s.split(),[],{}
  for i in s:f[i]=s.count(i)
  for n in sorted(f.items(),key=lambda o:o[1],reverse=True):v.append(n[0])
  return " ".join(str(v.index(z)+1)for z in s)