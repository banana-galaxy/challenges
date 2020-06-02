'''import os, random, json, testcases
from biz import validate

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
        if f != "testcases.py":
            unit = __import__(f"{f.split('.')[0]}")
            passed = True
            for i in keys:
                if type(i) == bool:
                    print(i)
                if i != 0:
                    try:
                        if unit.validate(i) != tests[i]:
                            passed = False
                            # check where specific solution get's tripped
                            #if f == "alanhong.py":
                            #    wrong.append(f"{f.split('.')[0]},{i} {tests[i]} {unit.validate(i)}")
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
#for i in checks:
#    print(i)
for i in wrong:
    print(i)
print("\n\n\nresults:\n")
for i in peeps:
    print(i)
print(f"passed {passs}\nnot passed {no_pass}")


import json
with open("second.json") as f:
    second = json.load(f)
with open("first.json") as f:
    first = json.load(f)
for x in second:
    if x not in first:
        print(x)'''

import os, random, json, testcases
import threading

from biz import validate


class Storage:
    def __init__(self):
        self.passed = True

def check(i, storage):
    if type(i) == bool:
        print(i)
    if i != 0:
        try:
            if unit.validate(i) != tests[i]:
                storage.passed = False
                # check where specific solution get's tripped
                # if f == "alanhong.py":
                #    wrong.append(f"{f.split('.')[0]},{i} {tests[i]} {unit.validate(i)}")
        except:
            storage.passed = False

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
        if f != "testcases.py":
            unit = __import__(f"{f.split('.')[0]}")
            storage = Storage()
            threads = []
            for i in keys:
                thread = threading.Thread(target=check, args=(i, storage))
                thread.start()
                threads.append(thread)
            for thread in thread:
                thread.join()
            if storage.passed:
                peeps.append(f.split('.')[0])
                passs += 1
            else:
                no_pass += 1
'''with open("second.json", 'w') as f:
    json.dump(peeps, f)'''
print("\n\n\n")
#for i in checks:
#    print(i)
for i in wrong:
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
        print(x)'''