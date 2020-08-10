def solution(a, r=0):
 for n,x in enumerate(a[1:]):
  g=n+1;l,b=a[n],a[g]
  if x<=l:a[g]=l+1;r+=a[g]-b
 return r