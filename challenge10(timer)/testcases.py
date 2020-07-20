import random


def gen(amount=50000):
    testcases = []
    for o in range(amount):  # amount of test cases
        print(f"generating cases {o + 1}/{amount}", end="\r")
        case = random.randint(5, 1439)
        testcases.append(case)
    return testcases


if __name__ == "__main__":
    cases = gen(3)
    for case in cases:
        print(case)
    #print(cases)#, [__import__("check").matrixSum(i) for i in cases])
