import os
import testcases
import time
import copy
from termcolor import colored
from check import fill, fill2
import sys
import update_board
from pathlib import Path

# Disable print
def disablePrint():
    sys.stdout = open(os.devnull, 'w')

# Restore print
def enablePrint():
    sys.stdout = sys.__stdout__

# initializing variables
start = time.time()
files = os.listdir(os.path.dirname(os.path.realpath(__file__)))
forbidden = ["check.py", "find.py", "test.py", "testcases.py"]
for x in forbidden:
    files.remove(x)
winners = []
try:
    # generating test cases and assigning the correct answers
    checks = testcases.gen()
    print()
    outs = []
    outs2 = []
    for check in checks:
        outs.append(fill(check))
        outs2.append(fill2(check))


    # testing
    ti=0
    wrong = []
    for index, f in enumerate(files):
        if f.endswith(".py"):
            starteff = time.time()
            try:
                unit = __import__(f.split('.')[0])
            except BaseException as e:
                wrong.append(f"{f.split('.')[0]}\nerror on interpretting:{e}")
                continue
            passed = True
            passed2 = True
            count = 0
            for i, x in enumerate(checks):
                print(f"solution: {index+1}/{len(files)} testcase: {i+1}/{len(checks)}  passed:{len(winners)} failed:{len(wrong)}", " "*len(str(len(checks))), end="\r")
                case = copy.deepcopy(x)
                if count < 1:
                    try:
                        disablePrint()
                        output = unit.fill(case)
                        enablePrint()
                        if output != outs[i]:
                            passed = False
                            if output != outs2[i]:
                                passed2 = False
                                wrong.append(f"\n{f.split('.')[0]}\ntest:{x}\nsolution output:{output}\ncorrect output:{outs[i]}")
                                count += 1
                    except BaseException as e:
                        enablePrint()
                        passed = False
                        passed2 = False
                        wrong.append(f"\n{f.split('.')[0]}\ntest:{x}\nerror:{e}\ncorrect output:{outs[i]}")
                        count += 1
                else:
                    count = 0
                    break
            endeff = time.time()
            if passed:
                winners.append([endeff - starteff, f.split('.')[0]])
            elif passed2:
                winners.append([endeff - starteff, f"{f.split('.')[0]} special pass :)"])
            ti = i
    print(f"solution: {index + 1}/{len(files)} testcase: {ti + 1}/{len(checks)}  passed:{len(winners)} failed:{len(wrong)}", " "*len(str(len(checks))), end="\r")
    end = time.time()

    # printing results
    print("\n\n\nFailed tests:")
    for i in wrong:
        print(i)

    print("\n\nWinners (sorted by code efficiency): ")
    for i in sorted(winners):
        print(colored(f"{i[0]:.2f}","white"), f"{i[1]}")

    # shortest solution
    shortest = ""
    solutions = []
    for sol in winners:
        sol = f"{sol[1]}.py"
        with open(sol) as f:
            solutions.append([f.read(), sol])
    for i, sol in enumerate(solutions):
        if i == 0:
            chars = len(sol[0])
            shortest = sol[1]
            continue
        if len(sol[0]) < chars:
            chars = len(sol[0])
            shortest = sol[1]
    short = []
    for i, sol in enumerate(solutions):
        if len(sol[0]) == chars and shortest != sol[1]:
            if short == []:
                short.append(shortest)
            short.append(sol[1])
    if short == []:
        print(f"\nshortest solution: {shortest.split('.')[0]}")
    else:
        print(f"\nshortest solutions:")
        for i in short:
            print(i.split('.')[0])

    print(f"\nComputation time: {end-start:.3f} seconds")
except KeyboardInterrupt:
    print("\nAborted")

usr = input("\n\nUpdate leaderboard? [Y/n] ")
if usr.lower() != "n":
    file = os.path.join(Path(os.path.dirname(os.path.realpath(__file__))).parent, "data.json")
    for i in winners:
        update_board.won(file, i[1], 9)
    for i in wrong:
        i = i.split("\n")[1]
        update_board.lost(file, i, 9)
    print("leaderboard updated")
else:
    print("leaderboard stays as is")