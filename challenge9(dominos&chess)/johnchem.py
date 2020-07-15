def fill(board):
def next_Empty_Cell(X, Y):
if X < dimX-1:
if board[posy][posx+1] == 0:
return (X+1, Y)
if Y < dimY-1:
if board[posy+1][posx] == 0:
return (X,Y+1)
return False

dimY, dimX = len(board), len(board[0])
valueTable = sum([i for row in board for i in row])
availablePosition = dimX*dimY-valueTable

if not availablePosition%2 == 0:
return False
else:
posx, posy = 0, 0
for posy in range(dimY):
for posx in range(dimX):
if board[posy][posx] == 0:
nextCell = next_Empty_Cell(posx, posy)
if not nextCell == False:
board[posy][posx] = 2
board[nextCell[1]][nextCell[0]] = 2
else:
return False
return False