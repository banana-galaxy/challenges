def solution(a):
 l=a[0];t=0
 for x in a[1:]:l,t=(x,t)if x>l else(l+1,t+l-x+1)
 return t