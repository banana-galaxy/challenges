def solution(k, ls):
    def gcd(a, b):
        if b == 0: return a
        return gcd(b, a%b)

    rn = len(ls)
    primes = [0] * (rn + 1)
    for i in range(rn):
        tmp_gcd = gcd(ls[i], ls[i+1])
        if tmp_gcd != ls[i]:
            primes[i+1] = tmp_gcd
            for j in range(i+2, rn+1):
                primes[j] = ls[j-1] // primes[j-1]
            for j in range(i, -1, -1):
                primes[j] = ls[j] // primes[j+1]

            break

    prime_set = sorted(set(primes))

    ans = ''
    for prime in primes:
        ans += chr(65+(prime_set.index(prime)))
    return ans