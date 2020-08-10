def inc(a):
    t=0
    for i in range(len(a)-1):
        b=a[i+1]
        a[i+1]=1+a[i]if b<a[i]else b
        j=a[i+1]-b
        t+=j
    return t