def whichExit(matrix):
    left = 0
    right = 0
    side = -1
    for row in matrix:
        if 0 not in row:
            continue
        for i in row:
            if i == 0:
                side = 1
            elif i == 1:
                if side == -1:
                    left += 1
                else:
                    right += 1
    return "left" if left<right else "right" if left>right else "same"

if __name__ == "__main__":
    print(whichExit([[1, -1, 1, -1, -1], [-1, -1, -1, 0, 1]]))