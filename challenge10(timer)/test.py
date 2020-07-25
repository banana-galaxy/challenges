import os
import testcases
import time
import copy
from termcolor import colored
from check import lateRide
import sys
import update_board
from pathlib import Path
import importlib

# Disable print
def disablePrint():
    sys.stdout = open(os.devnull, 'w')

# Restore print
def enablePrint():
    sys.stdout = sys.__stdout__

# initializing variables
start = time.time()
files = os.listdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), "solutions"))
winners = []
forbidden = ["__init__.py"]
disqualified = []
for i in forbidden:
    if i in files:
        files.remove(i)

try:
    # generating test cases and assigning the correct answers
    checks = testcases.gen(400000)
    print()
    outs = []
    for check in checks:
        outs.append(lateRide(check))


    # testing
    wrong = []
    for index, f in enumerate(files):
        if f.endswith(".py"):
            if f in disqualified:
                wrong.append(f"\n{f.split('.')[0]}\ndisqualified for disrespecting/disobeying staff or breaking the rules")
                continue
            starteff = time.time()
            try:
                unit = importlib.import_module(f".{f.split('.')[0]}", "solutions")
            except BaseException as e:
                wrong.append(f"\n{f.split('.')[0]}\nerror during interpretation: {e}")
                continue
            for i, x in enumerate(checks):
                print(f"solution: {index+1}/{len(files)} testcase: {i+1}/{len(checks)}  passed:{len(winners)} failed:{len(wrong)}", " "*len(str(len(checks))), end="\r")
                case = copy.deepcopy(x)
                try:
                    disablePrint()
                    output = unit.lateRide(case)
                    enablePrint()
                    if output != outs[i]:
                        wrong.append(f"\n{f.split('.')[0]}\ntest:{x}\nsolution output:{output}\ncorrect output:{outs[i]}")
                        break
                except BaseException as e:
                    enablePrint()
                    wrong.append(f"\n{f.split('.')[0]}\ntest:{x}\nerror:{e}\ncorrect output:{outs[i]}")
                    break
            else:
                endeff = time.time()
                winners.append([endeff - starteff, f.split('.')[0]])
    print(f"solution: {index + 1}/{len(files)} testcase: {i + 1}/{len(checks)}  passed:{len(winners)} failed:{len(wrong)}", " "*len(str(len(checks))), end="\r")
    end = time.time()
except KeyboardInterrupt:
    try:
        print("\nStopping halfway through")
        for i in range(3):
            print(f"{3-i} ", end="\r")
            time.sleep(1)
        print(" ", end="\r")
        end = time.time()
    except KeyboardInterrupt:
        print("\nAborted")
        quit()

# printing results
print("\n\n\nFailed tests:")
for i in wrong:
    print(i)

# winner solutions by efficiency first, then by length
print("\n\nWinners\nsorted by code efficiency: ")
for i in sorted(winners):
    print(colored(f"{i[0]:.2f}","white"), f"{i[1]}")

shortest = ""
solutions = []
for sol in winners:
    sol = os.path.join("solutions", f"{sol[1]}.py")
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
while len(short) < len(solutions):
    for sol in solutions:
        if len(sol[0]) == chars:
            short.append([len(sol[0]), sol[1]])
    chars+=1


print(f"\nsorted by code length:")
for i in short:
    print(i[0], i[1].split('.')[0].split('/')[1])

compTime = end-start
min = f"{compTime//60:.0f}"
sec = f"{compTime%60:.0f}"
print(f"\nComputation time: {min}:{sec if len(sec)==2 else '0'+sec}")

usr = input("\n\nUpdate leaderboard? [Y/n] ")
if usr.lower() != "n":
    file = os.path.join(Path(os.path.dirname(os.path.realpath(__file__))).parent, "data.json")
    for i in winners:
        update_board.won(file, i[1], 10)
    for i in wrong:
        i = i.split("\n")[1]
        update_board.lost(file, i, 10)
    print("leaderboard updated")
else:
    print("leaderboard stays as is")
