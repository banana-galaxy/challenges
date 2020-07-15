import random


def gen(amount=1000):
    testcases = []
    for o in range(amount):  # amount of test cases
        print(f"generating cases {o + 1}/{amount}", end="\r")
        case = []
        height = random.randint(3, 10)
        width = random.randint(3, 10)
        for h in range(height):
            case.append([])
            for _ in range(width):
                case[h].append(random.choice([-1, 1]))

        youX = random.randint(0, width-1)
        youY = random.randint(0, height-1)
        case[youY][youX] = 0

        testcases.append(case)
    return testcases


if __name__ == "__main__":
    cases = gen(3)
    for case in cases:
        for i, row in enumerate(case):
            if i == len(case)-1:
                print(f"{row}]")
            elif i == 0:
                print(f"[{row}")
            else:
                print(f"{row}")
    #print(cases)#, [__import__("check").matrixSum(i) for i in cases])
