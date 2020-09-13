def solution(a):
    x,y=0,0
    for dr in a:x,y={'n':(x,y+1),'e':(x+1,y),'s':(x,y-1),'w':(x-1,y)}[dr]
    return len(a)<=10 and x==y==0