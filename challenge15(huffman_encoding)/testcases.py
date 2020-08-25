import random
import string


from random import randint as r
from random import choices as cs
from random import choices as c
from string import ascii_letters as asc

def gen(amount):
    learn_yield = []
    for _ in range(amount):
        print(f"generating cases {_ + 1}/{amount}", end="\r")
        words = [[c(asc)[0] for _ in range(r(1,10))]for _ in range(r(1,5))]
        lol = lambda:r(1,100)
        case=cs(words,[lol() for x in " "*len(words)],k=r(1,20))
        learn_yield.append(" ".join(["".join(x) for x in case]))
    return learn_yield

'''def gen(amount=50000):
    testcases = []
    for o in range(amount):  # amount of test cases
        print(f"generating cases {o + 1}/{amount}", end="\r")
        case = ''
        
        testcases.append(case)
    return testcases'''


if __name__ == "__main__":
    cases = gen(3)
    print()
    for case in cases:
        print(case)
    #print(cases)#, [__import__("check").matrixSum(i) for i in cases])
