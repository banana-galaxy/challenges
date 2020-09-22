def solution(number: int, encrypted: list) -> str:
    def sieve(n: int) -> list:
        prime = [True for _ in range(n + 1)]
        p = 2
        while (p * p < n + 1):
            if prime[p]:
                for i in range(p * 2, n + 1, p):
                    prime[i] = False

            p += 1

        prime[0] = False
        prime[1] = False

        out = []

        for p in range(2, n + 1):
            if prime[p]:
                out.append(p)

        return out

    def hcf(x: int, y: int) -> int:
        while(y):
            x, y = y, x % y

        return x

    primes_included = set()
    for x, y in zip(encrypted, encrypted[1:]):
        if x == y:
            continue

        primes_included.add(hcf(x, y))

    i = 0
    first = encrypted[0] // hcf(encrypted[0], encrypted[1])
    while first == 1:
        first = encrypted[i] // hcf(encrypted[i], encrypted[i + 1])
        i += 1

    primes_included.add(first)

    i = -1
    last = encrypted[i] // hcf(encrypted[i], encrypted[i - 1])
    while last == 1:
        last = encrypted[i] // hcf(encrypted[i], encrypted[i - 1])
        i -= 1

    primes_included.add(last)

    if len(primes_included) < 26:
        primes = sieve(number)
        primes = [x for x in primes if x <= max(primes_included)][-26:]

    else:
        # sort to the alphabet
        primes = list(primes_included)
        primes.sort()

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out_mapping = [primes.index(first)]
    for prod in encrypted:
        second = prod // first
        out_mapping.append(primes.index(second))

        first = second

    return "".join([letters[x] for x in out_mapping])