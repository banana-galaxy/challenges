def solution(n,l):
 x=[]
 g=lambda a,b:a if b<1else g(b,a%b)
 p=lambda x:all(x%i!=0for i in range(int(x**0.5)+1)[2:])
 for i in range(len(l)-1):
  y=g(l[i],l[i+1])
  j=i
  if l[i]//y==1:
   if i>0:z=x[i-1][1];x.append((z,l[i]//z))
   else:
    while l[j]/y==1:
     j+=1
    k=g(l[j],l[i])
    x.append((l[i]//k,k))
  else:x.append((l[i]//y,y))
 s=x[-1][1]
 x.append((s,l[-1]//s))
 a,z=max(i[0]for i in sorted(x)if i[0]>1),max(i[1]for i in sorted(x)if i[1]>1)
 z=max(a,z)
 c=1
 d={}
 for i in range(z,1,-1):
  if c<27:
   if p(i):
    d[i]=chr(91-c)
    c+=1
 r=[]
 for i in x:
  r.append(d.get(i[0]))
 r.append(d.get(x[-1][1]))
 return ''.join(r)