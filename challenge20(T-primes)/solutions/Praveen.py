def solution(l):
    n=l**0.5
    if (n <= 1):
        return False
    i = 2
    while(i * i <= n):
        if n % i == 0:
            return False
        i += 1
    return True and l == int(n + 0.5)**2