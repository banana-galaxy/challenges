import os
import testcases
import time
import copy
from check import matrixSum

# initializing variables
start = time.time()
files = os.listdir(os.path.dirname(os.path.realpath(__file__)))
passs = 0
no_pass = 0
peeps = []
efficient = []
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
            print(f"solution: {index+1}/{len(files)} testcase: {i+1}/{len(checks)}    ", end="\r")
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
        efficient.append([endeff-starteff, f])
        if passed:
            peeps.append(f.split('.')[0])
            passs += 1
        else:
            no_pass += 1
end = time.time()

# printing results and stats
print("\n\n\n")
for i in wrong:
    print(i)
print("\n\n\nresults:\n")
for i in peeps:
    print(i)
print(f"\npassed {passs}\nnot passed {no_pass}")

print("\n\nStats:")
print(f"\nComputation time: {end-start:.3f} seconds")
print("\nEfficiency: ")
for i in sorted(efficient):
    found = False
    for w in wrong:
        if i[1].split(".")[0] in w:
            found = True
    if not found:
        print(f"{i[0]:.4f} {i[1]}")
