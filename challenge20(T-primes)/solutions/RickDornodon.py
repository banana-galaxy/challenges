# lambda
unbound=lambda n:n==4or(m:=n**.5)==int(m)>1and 1-any(n%i<1for i in range(2,int(m**.5)+1))
def sieve(limit):
    a = [1] * limit
    a[0] = a[1] = 0
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i * i
            for n in range(i * i, limit, i): a[n] = 0

s = sorted(sieve(5623))

def solution(n):
    if n > 10**15:
        return unbound(n)
    if n == 4:
        return 1
    if n == 1 or n % 2 < 1 or (m := n ** .5) != int(m):
        return 0
    for i in s:
        if i > m:
            break
        if n % i < 1:
            return 0
    return 1