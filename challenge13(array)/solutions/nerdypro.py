def solution(array):
moves = 0
for a in range(len(array)-1):
if array[a]>=array[a+1]:
t = array[a]-array[a+1]+1
array[a+1] += t
moves += t

return moves