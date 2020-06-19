'''import os, infernus, random, json

files = os.listdir(os.path.dirname(os.path.realpath(__file__)))
passs = 0
no_pass = 0
peeps = []

tests = {}
for i in range(1000):
    num = random.randint(0, 9000)
    tests[num] = infernus.yearToCentury(num)
tests[0] = 0
tests[600] = 6
tests[501] = 6
tests[499] = 5
checks = []

keys = tests.keys()

for f in files:
    if f.endswith(".py") and f != os.path.basename(__file__):
        unit = __import__(f"{f.split('.')[0]}")
        passed = True
        for i in keys:
            if i != 0:
                try:
                    if unit.yearToCentury(i) != tests[i]:
                        passed = False
                except:
                    passed = False
        if passed:
            peeps.append(f.split('.')[0])
            passs += 1
        else:
            no_pass += 1
with open("second.json", 'w') as f:
    json.dump(peeps, f)
print("\n\n\n")
for i in checks:
    print(i)
print("\n\n\nresults:\n")
for i in peeps:
    print(i)
print(f"passed {passs}\nnot passed {no_pass}")
'''

import json
with open("second.json") as f:
    second = json.load(f)
with open("first.json") as f:
    first = json.load(f)
for x in second:
    if x not in first:
        print(x)