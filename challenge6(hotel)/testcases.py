import random

def gen():
    cases = []
    for o in range(10000): # amount of test cases
        print(f"generating cases {o+1}/10000", end="\r")
        case = []
        height = random.randint(1, 40)
        width = random.randint(1, 40)
        for i in range(height):
            case.append([])
            for room in range(width):
                case[i].append(random.choice([0, random.randint(1, 100), random.randint(1, 1000), random.randint(1, 10000)]))
        cases.append(case)
    return cases

if __name__ == "__main__":
    print(gen())