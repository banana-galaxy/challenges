def solution(s):
    p=s.split(" ")
    q={}
    for w in p:q[w]=p.count(w)
    q=sorted(q.items(),key=lambda x: x[1],reverse=True)
    s=" "+s+" "
    for i in q:
        for x in range(i[1]):s=s.replace(" "+i[0]+" "," "+str(q.index(i)+1)+" ")
    return s[1:-1]