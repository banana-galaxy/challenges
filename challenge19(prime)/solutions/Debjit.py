def solution(n, l):
    def findAllPrimes(n):
        primes = [True for _ in range(n + 1)]
        p = 2
        while p * p <= n:
            if primes[p] == True:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        ans = []
        for i in range(2, n + 1):
            if primes[i]:
                ans.append(i)
        return ans

    pr = findAllPrimes(n)
    def assignCodes(mode, pr):
        lc = {}
        codes_used = []
        n = len(pr)
        if mode == "compensate":
            c, ascii = 1, 97
            for i in range(n):
                if c <= 26:
                    lc[pr[i]] = chr(ascii)
                    codes_used.append(pr[i])
                    ascii += 1
                    c += 1
        else:
            c,ascii = 1, 122
            for i in range(n-1, -1, -1):
                if c <= 26:
                    lc[pr[i]] = chr(ascii)
                    codes_used.append(pr[i])
                    ascii-=1
                    c+=1
        return lc, codes_used

    if len(pr) == 26:
        codes, ar = assignCodes("normal", pr)
    elif len(pr) > 26:
        codes, ar = assignCodes("normal", pr)
    else:
        codes, ar = assignCodes("compensate", pr)
    ar.sort()

    def primeFactorize(n):
        pf = []
        while n%2 == 0:
            pf.append(2)
            n = n//2
        for i in range(3, int(n**(1/2))+1, 2):
            while n%i == 0:
                pf.append(i)
                n=n//i
        if n > 2:
            pf.append(n)
        return pf
    for pn in l:
        f = primeFactorize(pn)
        print(codes[min(f)].upper(),end='')
    print(codes[max(primeFactorize(l[-1]))].upper())