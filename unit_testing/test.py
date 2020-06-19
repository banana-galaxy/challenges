import os

files = os.listdir(os.path.dirname(os.path.realpath(__file__)))

ins = [1, 2, 3]
outs = [2, 3, 4]

for f in files:
    if f.endswith(".py") and f != os.path.basename(__file__):
        unit = __import__(f"{f.split('.')[0]}")
        passed = True
        for i in range(len(ins)):
            try:
                if unit.test(ins[i]) != outs[i]:
                    passed = False
            except TypeError:
                passed = False
        if passed:
            print(f"{f} passed")
            