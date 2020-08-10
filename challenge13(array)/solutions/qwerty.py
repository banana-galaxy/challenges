def solution(a,i=0):
 for d in range(1,len(a)):
  while a[d-1]>=a[d]:a[d]+=1;i+=1
 return i