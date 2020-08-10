def solution(a):
m=0
if a:
for i in a:
while a[i]<=a[i-1]:
a[i]+=1
m+=1
return m