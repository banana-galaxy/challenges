def solution(d, f, s):
    a=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    d=a.index(d.title())
    f,s=[int(i)for i in f.split('/')],[int(i)for i in s.split('/')]
    l=(s[1]*30+s[0])-(f[1]*30+f[0])
    return a[(l+d)%7]