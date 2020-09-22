def solution(k, ls):
    primes = []
    ls_2 = []
    for i in ls:
        if i not in ls_2:
            ls_2.append(i)
    for i in range(1, len(ls_2)):
        primes.append(gcd(ls_2[i-1], ls_2[i]))

    primes.append(ls[0]//gcd(ls_2[0], ls_2[1]))
    primes.append(ls[-1]//gcd(ls_2[-1], ls_2[-2]))

    primes = list(set(primes))
    primes.sort()


    alphs = dict()
    for i, val in enumerate(primes):
        alphs[val] = chr(65+i)

    print(primes)
    for key in alphs:
        print(key, alphs[key])

    ans = ''
    for i in range(1, len(ls)):
        ans += alphs[gcd(ls[i-1], ls[i])]

    first = ls[0]//gcd(ls[0], ls[1])
    last = ls[-1]//gcd(ls[-1], ls[-2])

    final = alphs[first] + ans + alphs[last]
    return ans