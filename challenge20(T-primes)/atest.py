from testcases import gen
import json
from check import solution

array = gen(3000000)
cases = [array, []]

for case in cases[0]:
    cases[1].append(solution(case))

with open("tests.json", 'w') as f:
    json.dump(cases, f)