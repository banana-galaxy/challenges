import os, importlib
import update_board
from pathlib import Path

def solution(matrix, out=64):
    scale = int(out/len(matrix))
    return [[matrix[i//scale][n//scale] for n in range(out)] for i in range(out)]

def create_matrix(length):
   return [[n for n in range(1, length+1)] for i in range(length)]


factors = [2,4,8,16,32,64]
tests = [create_matrix(x) for x in factors]

myDir = os.listdir()

currentFile = os.path.basename(__file__)

answers = [solution(test) for test in tests]

passed = dict()
failed = dict()
for itr1 in myDir:
    if itr1 != currentFile and itr1 != "update_board.py":
        if itr1.endswith('.py'):
            itr1 = itr1[:itr1.index('.py')]
            myModule = importlib.import_module(itr1)
            results = [myModule.solution(test)==answers[index] for index, test in enumerate(tests)]
            if any(results):
                passed[itr1] = [results]
            else:
                failed[itr1] = results
print('passed:')
for fname in passed:
    print(fname, passed[fname])

print('\nfailed:')
for fname in failed:
    print(fname, failed[fname])

usr = input("\n\nUpdate leaderboard? [Y/n] ")
if usr.lower() != "n":
    file = os.path.join(Path(os.path.dirname(os.path.realpath(__file__))).parent, "data.json")
    for i in passed:
        update_board.won(file, i, 1)
    for i in failed:
        update_board.lost(file, i, 1)
    print("leaderboard updated")
else:
    print("leaderboard stays as is")