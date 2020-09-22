'''
this is the basic algorithm the unit test should follow:

import everything
choose the challenge to unit test
generate the test cases along with the answers
get all the submitted solution file names
test, store winners and fails in 2 different dicts
display fails and winners
'''
''' TODO 
fix bug where the unit test just doesn't go through any solutions, I think this has to do with how they are imported but at this point I don't know anymore

need to make a good reliable way/system to store the challenge results, probably with json, and some way that will be easy to manage

want/thought about having the unit test generate a simple html page to have a nicer way to view the results of the challenge

add in a time limit per solution, I have it done for the 20th challenge, just need to incorporate that here as well

would probably be nice to incorporate Biz's unit tester in here  
'''

import os
import importlib
from copy import deepcopy
import sys
import time
from termcolor import colored

# Disable print
def disablePrint():
    sys.stdout = open(os.devnull, 'w')

# Restore print
def enablePrint():
    sys.stdout = sys.__stdout__

def search(root, target=None):
    content = os.listdir(root)
    if target is None:
        return content
    else:
        result = []
        for thing in content:
            if target in thing:
                result.append(thing)
        return result

def generate(challenge, amount=5000):
    testcases = importlib.import_module('.testcases', challenge)
    check = importlib.import_module('.check', challenge)
    checks = testcases.gen(amount)
    ans = []
    for i,x in enumerate(checks):
        print(f"retrieving the correct answers for the testcases {i+1}/{len(checks)}", end='\r')
        if isinstance(x, list):
            ans.append(check.solution(*x))
        else:
            ans.append(check.solution(x))
    return [checks, ans]

def length(challenge, solution, lines=False):
    with open(os.path.join(challenge, 'solutions', solution)) as f:
        if lines:
            return len(f.read())
        else:
            return sum(len(i) for i in f.read())

def test(challenge, cases, output=True):
    root = os.path.join(os.path.dirname(os.path.realpath(__file__)), challenge, "solutions")
    files = os.listdir(root)
    results = [[], []]
    lists = isinstance(cases[0][0], list)

    for i,file in enumerate(files):
        # try importing otherwise add to failed
        try:
            unit = __import__(f"{challenge}.solutions.{file.split('.')[0]}")
        except SyntaxError as e:
            quit('e')
        #    results[1].append([file.split('.')[0], 'None', 'None', f'Syntax error: {e}'])
        #    continue'''

        # start solution timer
        startsol = time.time()

        # loop through test cases
        for case in range(len(cases[0])):
            # print status
            print(f'solution {i+1}/{len(files)}, case {case}/{len(cases[0])}, passed {len(results[0])}, failed {len(results[1])} {" "*10}', end='\r')
            # make deep copy of test case so the original is not overridden
            testcase = deepcopy(cases[0][case])
            # disable printing while testing solution
            disablePrint()
            # testing current solution with current case
            try:
                if lists:
                    ans = unit.solution(*testcase)
                else:
                    ans = unit.solution(testcase)
                if ans != cases[1][case]:
                    results[1].append([file.split('.')[0], cases[0][case], cases[1][case], ans])
                    break
            except BaseException as e:
                results[1].append([file.split('.')[0], cases[0][case], cases[1][case], e])
                break
            enablePrint()
        # stop solution timer
        endsol = time.time()
        if file.split('.')[0] not in [i[0] for i in results[1]]:
            results[0].append([file.split('.')[0], length(challenge, file), length(challenge, file, True), f'{(endsol-startsol):.2f}'])

        return results



if __name__ == '__main__':
    # clear
    os.system('clear')

    # choose challenge to test
    id = search(os.path.dirname(os.path.realpath(__file__)), input('Challenge to test: '))
    usr = input(f'confirm {id[0]} [Y/n/list]')
    if usr == 'n':
        quit()
    elif usr == 'list':
        for i,x in enumerate(id):
            print(i,x)
        index = int(input('index: '))
        challenge = id[index]
    else:
        challenge = id[0]
    caseAmount = int(input('Amount of testcases: '))

    # generate cases with answers
    cases = generate(challenge, caseAmount)
    results = test(challenge, cases)
    #makePage(results)

    # print out the results
    correct = results[0]
    errors = results[1]

    print('Winners')
    for i in correct:
        print(f'{i[0]}, chars {i[1]}, lines {i[2]}, efficiency {i[3]}')



