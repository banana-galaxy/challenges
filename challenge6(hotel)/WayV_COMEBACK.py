matrixSum = lambda matrix: sum([col for row in [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))] for col in row[0:row.index(0) if 0 in row else len(row)]])

# Okay, that is the most ugliest function I have made and it doesn't explain my thinking.
# Hence, a normal function.
#
# def matrixSum(matrix):
#     #Getting the transpose of matrix i.e swapping the rows and columns
#     matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
#
#     cost = 0
#     #We travel through each element of matrix
#     for row in matrix:
#         for col in row:
#             #We don't want to consider any of the rooms BELOW a free room
#             #But since I took transpose, we don't want to consider any of the room
#             #RIGHT of or AFTER a free room
#             if col == 0:
#                 break
#             cost += col
#
#     return cost
#
# Yo, I swear, if I lose, I will cry :"(