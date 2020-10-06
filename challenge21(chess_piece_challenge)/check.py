def solution(s,e,n):
  if n>1:
    if(ord(s[0])+ord(e[0]))%2==0:
      if(int(s[1])+int(e[1]))%2==0:return 1
    elif(int(s[1])+int(e[1]))%2==1:return 1
  elif n==0:
    if s==e:return 1
  else:
    if abs(ord(e[0])-ord(s[0]))-abs(int(e[1])-int(s[1]))==0:return 1
  return 0