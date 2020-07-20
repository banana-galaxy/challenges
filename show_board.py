import os
import matplotlib.pyplot as plt
import json

file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data.json")
with open(file) as f:
    read = json.load(f)

data={}
users = read.keys()
for user in users:
    data[user]=0
    for chlngid in read[user].keys():
        data[user]+=read[user][chlngid]

data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

names = list(data.keys())
values = list(data.values())

fig, ax = plt.subplots()
ax.bar(names, values)

plt.xticks(rotation=80)
plt.show()