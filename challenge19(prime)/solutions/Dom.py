def solution(z: int, message: (list, tuple)) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def gcd(a, b):
        # euclidean gcd algo
        while b:
            a, b = b, a%b
        return a

    prior = 0
    i = 0
    while prior == 0:
        if message[i] != message[i+1]:
            low = min(message[i], message[i+1])
            high = max(message[i], message[i+1])
            prior = gcd(high, low)
        i += 1

    start = prior
    primes = [prior := val//prior for val in message[1:]]
    primes.insert(0, start)
    primes.insert(0, message[0]//start)

    decrypt = {p: alphabet[i] for i, p in enumerate(sorted(set(primes)))}

    return "".join([decrypt[p] for p in primes])