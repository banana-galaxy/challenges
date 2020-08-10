def solution(l,n=0):
 for i in range(1,len(l)):
  if l[i-1]>=l[i]:e=l[i-1]-l[i]+1;n+=e;l[i]+=e
 return n