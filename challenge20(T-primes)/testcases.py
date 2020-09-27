import random
from check import solution

def gen(amount=50000):
    testcases = []
    primes = []
    count = 0
    while len(primes)<50:
        if solution(count):
            primes.append(count)
        count += random.randint(1, 10)
        print(f"getting some T-primes for the generator {len(primes)}/50", end='\r')
    print()

    for o in range(amount):  # amount of test cases
        print(f"generating cases {o + 1}/{amount}", end="\r")
        case = random.choice([random.choice(primes), random.randint(0,1000000), random.randint(0, 2)])
        testcases.append(case)
    return testcases


if __name__ == "__main__":
    cases = gen(3)
    print()
    for case in cases:
        print(case)
    #print(cases)#, [__import__("check").matrixSum(i) for i in cases])
