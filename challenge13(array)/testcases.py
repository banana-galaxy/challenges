import random


def gen(amount=50000):
    testcases = []
    for o in range(amount):  # amount of test cases
        print(f"generating cases {o + 1}/{amount}", end="\r")
        case = []
        length = random.randint(2, 12)
        units = random.choice([10, 100, 1000, 10000])
        for i in range(length):
            case.append(random.randint(units*-1, units))
        testcases.append(case)
    return testcases


if __name__ == "__main__":
    cases = gen(3)
    print()
    for case in cases:
        print(case)
    #print(cases)#, [__import__("check").matrixSum(i) for i in cases])
