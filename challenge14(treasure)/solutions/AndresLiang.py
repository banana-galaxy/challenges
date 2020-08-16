def solution(value1, weight1, value2, weight2, maxW):

    if maxW >= weight1+weight2: return value1+value2
    elif maxW >= weigth1 or weight2:
        if weight1<=maxW>=weight2:
            if value1>value2: return value1
            else: return value2
        else:
            if weight1<=maxW: return value1
            elif weight2<=maxW: return value2
            else: return 0
    else: return 0