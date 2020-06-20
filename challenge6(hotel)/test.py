import os
import testcases
import time
import copy
from check import matrixSum

# initializing variables
start = time.time()
files = os.listdir(os.path.dirname(os.path.realpath(__file__)))
winners = []
forbidden = ["testcases.py", "check.py", os.path.basename(__file__), "__pycache__", "find.py"]
for i in forbidden:
    if i in files:
        files.remove(i)

# generating test cases and assigning the correct answers
checks = testcases.gen()
print()
outs = []
for check in checks:
    outs.append(matrixSum(check))


# testing
wrong = []
for index, f in enumerate(files):
    if f.endswith(".py"):
        starteff = time.time()
        unit = __import__(f"{f.split('.')[0]}")
        passed = True
        count = 0
        for i, x in enumerate(checks):
            print(f"solution: {index+1}/{len(files)} testcase: {i+1}/{len(checks)}  passed:{len(winners)} failed:{len(wrong)}    ", end="\r")
            case = copy.deepcopy(x)
            if count < 1:
                try:
                    if unit.matrixSum(case) != outs[i]:
                        passed = False
                        wrong.append(f"{f.split('.')[0]},{x} {outs[i]} {unit.matrixSum(case)}")
                        count += 1
                except BaseException as e:
                    passed = False
                    wrong.append(f"{f.split('.')[0]},{x} {outs[i]} {e}")
                    count += 1
            else:
                count = 0
                break
        endeff = time.time()
        if passed:
            winners.append([endeff - starteff, f.split('.')[0]])
        print(f"solution: {index + 1}/{len(files)} testcase: {i + 1}/{len(checks)}  passed:{len(winners)} failed:{len(wrong)}    ",end="\r")
end = time.time()

# printing results
print("\n\n\nfailed tests:")
for i in wrong:
    print(i)

print("\nWinners (sorted by code efficiency): ")
for i in sorted(winners):
    print(f"{i[0]:.2f} {i[1]}")
print(f"\nComputation time: {end-start:.3f} seconds")
