import random


def gen(amount=50000, w: tuple = (3, 10), h: tuple = (3, 10), fil=10):
    testcases = []
    for o in range(amount):  # amount of test cases
        print(f"generating cases {o + 1}/{amount}", end="\r")
        case = []
        height = random.randint(*h)
        width = random.randint(w[0], w[1])
        for i in range(height):
            case.append([])
            for _ in range(width):
                case[i].append(0)
        fill = int(fil/100*(width*height))
        if fill <= 1:
            fill = 2
        fill = random.randint(1, fill)
        for i in range(fill):
            x, y = random.randrange(0,height), random.randrange(0,width)
            add = True
            for r in range(-1, 2):
                for t in range(-1, 2):
                    try:
                        if case[x+r][y+t] == 1:
                            add = False
                    except IndexError:
                        pass
            if add:
                case[x][y] = 1

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
