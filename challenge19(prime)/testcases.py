import random
import string
import sympy
import copy

def gen(amount=50000):
    testcases = []
    primes = list(sympy.primerange(1, 10000))
    for o in range(amount):  # amount of test cases
        print(f"generating cases {o + 2}/{amount+1}", end="\r")
        last = random.randint(25, len(primes)-2)
        case = []
        case.append(random.randrange(primes[last], primes[last+1]))
        chars = list(string.ascii_uppercase)
        random.shuffle(chars)
        extra = random.randint(0, 5)
        for i in range(extra):
            chars.append(random.choice(string.ascii_uppercase))
        encoded = []
        for i in range(1, len(chars)):
            char1_index = string.ascii_uppercase.index(chars[i-1])
            char2_index = string.ascii_uppercase.index(chars[i])
            encoded.append(primes[last-(25-char1_index)] * primes[last-(25-char2_index)])
        case.append(encoded)

        testcases.append(case)
    testcases.append([991, [210677, 210677, 210677, 210677, 210677, 210677, 210677, 213443, 216221, 223693, 233273, 239117, 245009, 250997, 256027, 265189, 272483, 282943, 295927, 304679, 313591, 320347, 324899, 329467, 338699, 348091, 355207, 359999, 364807, 372091, 378221]])
    return testcases


if __name__ == "__main__":
    cases = gen(3)
    print()
    for case in cases:
        print(case)
    #print(cases)#, [__import__("check").matrixSum(i) for i in cases])
