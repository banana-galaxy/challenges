def solution(s):
 if len(s)>10:return False
 d={p:s.count(p)for p in s}
 return d['n']==d['s']and d['e']==d['w']