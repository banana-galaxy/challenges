def solution(array):
moves = 0
for i in range(1, len(array)):
while array[i] <= array[i-1]:
moves = moves + 1
array[i] = array[i] + 1

return moves