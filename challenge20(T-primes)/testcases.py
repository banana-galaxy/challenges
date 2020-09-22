import random
import string

def gen(amount=50000):
    testcases = []
    primes = []
    count = 0
    solution = lambda n: (int(k := n ** .5) == k * all(k % i for i in range(2, int(k ** .5) + 1))) * n > 1
    while len(primes)<100:
        if solution(count):
            primes.append(count)
        count += random.randint(1, 10)
        print(f"getting some T-primes for the generator {len(primes)}/100", end='\r')
    print()

    for o in range(amount):  # amount of test cases
        print(f"generating cases {o + 1}/{amount}", end="\r")
        case = random.choice([random.choice(primes), random.randint(0,1000000000), random.randint(0, 2)])
        testcases.append(case)
    return testcases


if __name__ == "__main__":
    cases = gen(3)
    print()
    for case in cases:
        print(case)
    #print(cases)#, [__import__("check").matrixSum(i) for i in cases])
