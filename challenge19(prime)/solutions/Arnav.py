def f(n,e) :
    hm=[]
    for i in range (2, n):
        if (e % i == 0):
            hm.append(i)
            while (e%i == 0):
                e = e/i
    return hm
def solution(n,l) :
    c=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    Next=None
    for i in range(len(l)) :
        try:
            Next = [e for e in f(n,l[i])if e not in f(n,l[i+1])][0]
            break
        except : continue
    eee = [Next]
    for i in l :
        Next = i//Next
        eee.append(Next)
    d = dict(zip(sorted(set(eee)),c))
    return ''.join(d[i] for i in eee)