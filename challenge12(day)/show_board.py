import os, update_board
import matplotlib.pyplot as plt
from pathlib import Path

file = os.path.join(Path(os.path.dirname(os.path.realpath(__file__))).parent, "data.json")
data = update_board.get(file)

data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

names = list(data.keys())
values = list(data.values())

fig, ax = plt.subplots()
ax.bar(names, values)

plt.xticks(rotation=30)
plt.show()