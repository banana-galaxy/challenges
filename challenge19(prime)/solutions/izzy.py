def solution(_,l):
    g=lambda x,y:g(y,x%y)if y else x
    f=len(l)+1
    c=(f)*[-1]
    for i in range(f-2):
        d=g(l[i],l[i+1])
        if d!=l[i]:
            c[i+1]=d
            for w in range(i+2,f):c[w]=l[w-1]//c[w-1]
            for w in range(i,-1,-1):c[w]=l[w]//c[w+1]
    return"".join(chr(65+[*sorted(set(c))].index(o))for o in c)