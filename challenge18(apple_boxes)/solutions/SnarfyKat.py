def solution(k):

    numYellow = numRed = 0

    for i in range(1, k+1):
        applesInBox = i*i
        if (i % 2) == 0:
            numRed += applesInBox
        else:
            numYellow += applesInBox

    return numRed - numYellow