import random


def gen(amount=100000):
    testcases = []
    for o in range(amount):  # amount of test cases
        print(f"generating cases {o + 1}/{amount}", end="\r")
        case = []
        height = random.randint(1, 7)
        width = random.randint(1, 7)
        for i in range(height):
            case.append([])
            for room in range(width):
                case[i].append(
                    random.choice([0, random.randint(1, 100), random.randint(1, 1000), random.randint(1, 10000)]))
        testcases.append(case)
    return testcases


if __name__ == "__main__":
    cases = gen(3)
    print(cases, [__import__("check").matrixSum(i) for i in cases])
