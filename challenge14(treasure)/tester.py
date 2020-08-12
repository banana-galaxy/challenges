import json

print("Reading testcases file...")
with open("tests.json") as f:
    tests = json.load(f)

#solution function here

passed = 0
failed = []

print("Checking cases...")
for case in range(len(tests[0])):
    check = solution(*tests[0][case])
    if check == tests[1][case]:
        passed += 1
    else:
        failed.append([tests[0][case], tests[1][case], check])

print(f'passed {passed} cases out of {len(tests[0])}')

if len(failed) > 0:
    print('\n\ntop three failed cases:')
    for i in range(3):
        if i < len(failed):
            print(f'case:{failed[i][0]}\ncorrect answer:{failed[i][1]}\nsolution answer:{failed[i][2]}\n')