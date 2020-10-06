import random
from check import solution

def gen(amount=2000):
    g = lambda: f"{random.choice('abcdefgh')}{random.randint(1, 8)}"
    case = lambda: (g(), g(), random.choice([1, random.randint(1, 20)]))
    testcases = []
    for i in range(amount):
        print(f"Generating test {i+1}/{amount}", end='\r')
        testcases.append(case())
    return testcases


if __name__ == "__main__":
    cases = gen(3)
    print()
    for case in cases:
        print(case)
    #print(cases)#, [__import__("check").matrixSum(i) for i in cases])
