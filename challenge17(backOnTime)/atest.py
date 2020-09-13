from testcases import gen
import json

def solution(a):
    if len(a)>10:
        return False
    return a.count('n')==a.count('s')and a.count('e')==a.count('w')

array = gen(2000)
cases = [array, []]

for case in cases[0]:
    cases[1].append(solution(case))

with open("tests.json", 'w') as f:
    json.dump(cases, f)