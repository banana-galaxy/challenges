def fill(m):
    v=[(x,y) for x in range(len(m)) for y in range(len(m[x])) if m[x][y]==0];n=[];g=[]
    while len(v)>0 or len(n)>0:
        if len(n)==0:x,y=v.pop(0);n.append((x,y));g.append([(x,y)])
        else:
            x,y=n.pop(0)
            for a,b in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if 0<=a<len(m) and 0<=b<len(m[a]) and (a,b) in v:v.remove((a,b));n.append((a,b));g[-1].append((a,b))
    for p in g:
        if not (lambda p:sum([[1,-1][(i+j)%2] for i,j in p])==0)(p):return False
    return True