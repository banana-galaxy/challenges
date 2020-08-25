def solution(i):
  d=i.split();f={x:0 for x in d}
  for s in d:f[s]+=1
  f={k:v for k,v in sorted(f.items(),reverse=True,key=lambda item: item[1])};
  l=list(f.keys());f={p:l.index(p)+1 for p in f}
  r = ""
  for b in d:r += str(f[b]) + " "
  return r[0:-1]