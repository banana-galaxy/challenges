def solution(m,h,n):a,b,c,d=map(ord,m+h);x,y=abs(a-c),abs(b-d);return(x&1==y&1)&((x==y)+n>1)|(m==h)