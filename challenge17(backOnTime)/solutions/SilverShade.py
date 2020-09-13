def solution(x):
  c,ns,ew=[0,0],{'n':1,'s':-1},{'e':1,'w':-1}
  for j in x:
    if j in'ns':
      c[0]+=ns[j]
    else:
      c[1]+=ew[j]
  return c==[0, 0] and len(x)<11