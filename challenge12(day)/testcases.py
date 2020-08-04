import random


def gen(amount=50000):
    testcases = []
    for o in range(amount):  # amount of test cases
        print(f"generating cases {o + 1}/{amount}", end="\r")
        case = []
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        case.append(random.choice(days))
        case.append(f"{random.randint(1, 30)}/{random.randint(1, 12)}")

        last = f"{random.randint(1, 30)}/{random.randint(1, 12)}"
        while last == case[-1]:
            last = f"{random.randint(1, 30)}/{random.randint(1, 12)}"
        case.append(last)
        for date in range(1,3):
            check = case[date].split('/')
            for i in range(len(check)):
                if int(check[i]) < 10:
                    check[i] = "0" + check[i]
            case[date] = '/'.join(check)
        testcases.append(case)
    return testcases


if __name__ == "__main__":
    cases = gen(3)
    for case in cases:
        print(case)
    #print(cases)#, [__import__("check").matrixSum(i) for i in cases])
