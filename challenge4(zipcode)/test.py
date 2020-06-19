import os, random, json, testcases, time
from Alex import validate
start = time.time()
files = os.listdir(os.path.dirname(os.path.realpath(__file__)))
passs = 0
no_pass = 0
peeps = []

checks = testcases.gen()
tests = {}
for check in checks:
    tests[check] = validate(check)

keys = tests.keys()

wrong = []

for f in files:
    if f.endswith(".py") and f != os.path.basename(__file__):
        if f != "testcases.py" and f != "Alex.py":
            unit = __import__(f"{f.split('.')[0]}")
            passed = True
            count = 0
            for i in keys:
                if count < 1:
                    try:
                        if unit.validate(i) != tests[i]:
                            passed = False
                            wrong.append(f"{f.split('.')[0]},{i} {tests[i]} {unit.validate(i)}")
                            count += 1
                    except BaseException as e:
                        passed = False
                        wrong.append(f"{f.split('.')[0]},{i} {tests[i]} {e}")
                        count += 1
                else:
                    count = 0
                    break
            if passed:
                peeps.append(f.split('.')[0])
                passs += 1
            else:
                no_pass += 1
end = time.time()
print("\n\n\n")
for i in wrong:
    print(i)
print("\n\n\nresults:\n")
for i in peeps:
    print(i)
print(f"\npassed {passs}\nnot passed {no_pass}")
print(f"Computation time: {end-start} seconds")