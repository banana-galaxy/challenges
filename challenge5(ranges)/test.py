import os, random, json, time
start = time.time()
files = os.listdir(os.path.dirname(os.path.realpath(__file__)))
passs = 0
no_pass = 0
peeps = []


wrong = []

for f in files:
    if f.endswith(".py") and f != os.path.basename(__file__):
        if f != "CryptoKnight.py":
            unit = __import__(f"{f.split('.')[0]}")
            passed = True
            count = 0

            original = []
            test = []

            for _ in range(100): # 1000 tests
                if count < 1: # run through test is unit passed all tests so far
                    try:
                        func = random.choice(["range", "enumerate"])
                        if func == "range":
                            args = []
                            argLen = random.randint(1, 3)
                            for i, n in enumerate(range(argLen)):
                                args.append(random.randint(-20, 20))
                                if i == 1:
                                    delta = args[0] - args[1]
                                    while abs(delta) < 2:
                                        args[1] = random.randint(-20, 20)
                                        delta = args[0] - args[1]
                                elif i == 2:
                                    if args[1] > args[0]:
                                        if args[2] <= 0:
                                            args[2] = random.randint(1, 4)
                                    elif args[1] < args[0]:
                                        if args[2] >= 0:
                                            args[2] = random.randint(-4, -1)
                            if len(args) == 1:
                                if args[0] < 0:
                                    args[0] = random.randint(1, 20)
                                if list(unit.erange(args[0])) != list(range(args[0])):
                                    passed = False
                                    wrong.append(f"{f.split('.')[0]}, range({args[0]}), {list(range(args[0]))}, {list(unit.erange(args[0]))}")
                                    count += 1
                            elif len(args) == 2:
                                if args[1] < args[0]:
                                    args[1] = random.randint(30, 40)
                                if list(unit.erange(args[0], args[1])) != list(range(args[0], args[1])):
                                    passed = False
                                    wrong.append(f"{f.split('.')[0]}, range({args[0]}, {args[1]}), {list(range(args[0], args[1]))}, {list(unit.erange(args[0], args[1]))}")
                                    count += 1
                            elif len(args) == 3:
                                if list(unit.erange(args[0], args[1], args[2])) != list(range(args[0], args[1], args[2])):
                                    passed = False
                                    wrong.append(f"{f.split('.')[0]}, range({args[0]}, {args[1]}, {args[2]}), {list(range(args[0], args[1], args[2]))}, {list(unit.erange(args[0], args[1], args[2]))}")
                                    count += 1

                        elif func == "enumerate":
                            listLen = random.randint(2, 40)
                            n = random.randint(0, 1)
                            if n:
                                startn = random.randint(2, 40)
                                if list(unit.numerate(list(range(listLen)), startn)) != list(enumerate(list(range(listLen)), startn)):
                                    passed = False
                                    wrong.append(f"{f.split('.')[0]}, enumerate(list(range({listLen})), {startn}), {list(enumerate(list(range(listLen)), startn))}, {list(unit.numerate(list(range(listLen)), startn))}")
                                    count += 1
                            else:
                                if list(unit.numerate(list(range(listLen)))) != list(enumerate(list(range(listLen)))):
                                    passed = False
                                    wrong.append(f"{f.split('.')[0]}, enumerate(list(range({listLen})), {list(enumerate(list(range(listLen))))}, {list(unit.numerate(list(range(listLen))))}")
                                    count += 1
                    except BaseException as e:
                        print(f"{f.split('.')[0]} {args} {func} {e}")
                        if func == "range":
                            if len(args) == 1:
                                wrong.append(f"{f.split('.')[0]}, range({args[0]}), {list(range(*args))}, {e}")
                            elif len(args) == 2:
                                wrong.append(f"{f.split('.')[0]}, range({args[0]}, {args[1]}), {list(range(*args))}, {e}")
                            elif len(args) == 3:
                                wrong.append(f"{f.split('.')[0]}, range({args[0]}, {args[1]}, {args[2]}), {list(range(*args))}, {e}")
                        elif func == "enumerate":
                            if n:
                                wrong.append(f"{f.split('.')[0]}, enumerate(list(range({listLen})), {n}), {list(enumerate(list(range(listLen)), n))}, {e}")
                            else:
                                wrong.append(f"{f.split('.')[0]}, enumerate(list(range({listLen}))), {list(enumerate(list(range(listLen))))}, {e}")
                        passed = False
                        count += 1
                else:
                    count = 0
                    break
        else:
            passed = False
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