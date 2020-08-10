def solution(l):
moves = 0
for x in range(len(l)-1):
if l[x] >= l[x+1]:
moves += (l[x]-l[x+1])+1
l[x+1] +=(l[x]-l[x+1])+1
return moves