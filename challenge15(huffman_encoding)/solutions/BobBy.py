def solution(x):
    a,c,d,e,o,m,h=x.split(),[],[],[],[],1,''
    for x in a:
        if x not in c:
            c.append(x)
            e.append(0)
    for i in c:d.append(a.count(i))
    for j in range(max(d),0,-1):
        q = 0
        for i in d:
            if i==j:
                e[q]=m
                m+=1
            q+=1
    for i in a:
        n=0
        for j in c:
            if j==i:o.append(e[n])
            n+=1
    for j in o:h+=' '+str(j)
    return h.strip()