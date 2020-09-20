def solution(k):
    yellowApples, redApples = 0, 0
    for m in range(1, k+1):
        if m % 2 == 0:
            redApples = redApples + (m*m)
        else:
            yellowApples = yellowApples + (m*m)
    return (redApples-yellowApples)