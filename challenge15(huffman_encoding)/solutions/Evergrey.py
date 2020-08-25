def solution(s):
myDict = {x: 0 for x in s.split()}
for word in s.split():
myDict[word] -= 1
for counter in range(1, len(myDict)+1):
smallest = min(myDict.values())
for k, v in myDict.items():
if v >= 0:
continue
elif v == smallest:
myDict[k] = counter
for key in myDict:
s = s.replace(key, str(myDict[key]))
return s