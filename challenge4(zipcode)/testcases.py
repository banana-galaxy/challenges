import random, string

def gen():
    cases = []
    for _ in range(10000): # amount of test cases
        for i in range(1, 11):
            case = ""
            for x in range(i):
                num = random.randint(0, 9)
                case += str(num)
            cases.append(case)
    
    for i in range(len(cases)):
        if i%2 == 0:
            cases[i] = int(cases[i])

    for i in range(len(cases)):
        if random.randint(1, 3) == 2:
            integer = False
            if type(cases[i]) == int:
                integer = True
            if integer:
                cases[i] = str(cases[i])
            case = []
            for char in cases[i]:
                case.append(char)
            amount = random.randint(1, len(case))
            for _ in range(amount):
                index = random.randint(0, len(case)-1)
                char = random.choice(string.ascii_lowercase)
                case[index] = char
            cases[i] = "".join(case)
    return cases

if __name__ == "__main__":
    print(gen())