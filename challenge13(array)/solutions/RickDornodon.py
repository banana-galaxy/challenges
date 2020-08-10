def solution(i):
 a=0;x=i[0]-1
 for v in i:
  if v<=x:a+=x-v+1;v+=1
  x=v
 return a