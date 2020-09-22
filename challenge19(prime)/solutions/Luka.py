def GCD(a,b):
    if b==0:return a
    else:return GCD(b,a%b)

def solution(n,l):
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if l[0]!=l[1]:
        o = GCD(l[0],l[1])
        R = [l[0]/o,o,l[1]/o]
    else:
        for i in range(len(l)):
            if l[0]!=l[i]:
                o=GCD(l[i-1],l[i])
                R=[l[i-1]/o,o,l[i-1]/o]
                break
    for i in range(2,len(l)):
        R+=[l[i]/R[-1]]
    l= sorted(list(set(R)))
    return "".join([a[l.index(i)] for i in R])