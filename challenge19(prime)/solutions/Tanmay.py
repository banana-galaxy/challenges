def solution(prime_limit, products_lst):
    primes, output_str = [], ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for k in range(24):
        a, b = products_lst[k], products_lst[k+1]
        while b:
            a, b = b, a%b
        primes.append(a)

    primes.insert(0, products_lst[0] // primes[0])
    primes.append(products_lst[-1] // primes[-1])
    ordered = sorted(primes)

    for elem in primes:
        index = ordered.index(elem)
        output_str += alphabet[index]

    return output_str