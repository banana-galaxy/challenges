def solution(baseprime,primes):
    def isprime(n):
        isprime=True
        for i in range(2,n-1):
            if n%i == 0:
                isprime=False
        return isprime
    if isprime(baseprime):
        cipherkey = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        decrypted_text=''
        letters={}
        x=0
        n=baseprime+1
        for l in cipherkey:
                while isprime(n) == False:
                    n += 1


                letters[l] = n
                n += 1
        #print(letters)
        for prime in primes:
            for key in cipherkey:
                if letters[key] == prime:
                    decrypted_text += key
        return decrypted_text

    else:
        raise ValueError("invalid number, number must be a prime!")