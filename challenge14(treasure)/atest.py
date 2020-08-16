from testcases import gen
import json

solution=lambda a,b,c,d,e:max(a*(b<=e),c*(d<=e),(a+c)*(b+d<=e))

array = gen(2000)
cases = [array, []]

for case in cases[0]:
    cases[1].append(solution(*case))

with open("tests.json", 'w') as f:
    json.dump(cases, f)