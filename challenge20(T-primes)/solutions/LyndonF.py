def isPrime(n):
    if n in [0,1,4,6,8,9] or n%2==0:
        return False
    elif n in [2,3,5,7]:
        return True
    i = 3
    while i*i<=n:
        if n%i==0:
            return False
        i += 2
    return True

def solution(n):
    sq = n**0.5
    sq = sq - sq%1
    if sq*sq==n:
        return isPrime(sq)
    elif (sq+1)*(sq+1)==n:
        return isPrime(sq+1)
    else:
        return False