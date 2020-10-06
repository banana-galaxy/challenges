def solution(s,e,n):
    if n==0:
        if s==e:
            return True
        else:
            return False
    if (ord(s[0])%2==ord(s[1])%2) == (ord(e[0])%2==ord(e[1])%2) and (n>=2 or abs(ord(s[0])-ord(e[0]))==abs(ord(s[1])-ord(e[1]))):
        return True
    else:
        return False