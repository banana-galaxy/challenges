import random
import string

def gen(amount=50000):
    testcases = []
    for o in range(amount):  # amount of test cases
        print(f"generating cases {o + 1}/{amount}", end="\r")
        case = random.randint(3, 1000)
        testcases.append(case)
    return testcases


if __name__ == "__main__":
    cases = gen(3)
    print()
    for case in cases:
        print(case)
    #print(cases)#, [__import__("check").matrixSum(i) for i in cases])
