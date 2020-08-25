def solution(t,x={}):
 for i in t.split():x[i]=x[i]+1if i in x else 1
 s=[k for k,v in sorted(x.items(),key=lambda s:s[1],reverse=True)]
 return" ".join(str(s.index(i)+1)for i in t.split())