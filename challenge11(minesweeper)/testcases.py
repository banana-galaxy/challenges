import random


def gen(amount=50000):
    testcases = []
    for o in range(amount):  # amount of test cases
        print(f"generating cases {o + 1}/{amount}", end="\r")
        case = []
        width = random.randint(0,20)
        height = random.randint(0,20)
        for h in range(height):
            case.append([])
            for w in range(width):
                case[h].append(0)
        percentage = random.randint(1,70)
        mines_amount = int(width*height/100*percentage)
        print(mines_amount, width, height, percentage)
        for i in range(mines_amount):
            x = random.randrange(0,len(case[0]))
            y = random.randrange(0,len(case))
            if case[y][x] == 'x':
                while case[y][x] == 'x':
                    x = random.randrange(0, len(case[0]))
                    y = random.randrange(0, len(case))
            case[y][x] = 'x'
        testcases.append(case)
    return testcases


if __name__ == "__main__":
    cases = gen(3)
    for case in cases:
        print(case)
    #print(cases)#, [__import__("check").matrixSum(i) for i in cases])
