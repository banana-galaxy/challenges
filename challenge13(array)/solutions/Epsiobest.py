def solution(l,c=0):
 for i in range(1,len(l)):
  while l[i-1]>=l[i]:l[i]+=1;c+=1
 return c