def solution(value1, weight1, value2, weight2, maxW):
    if weight1+weight2 == maxW  or weight1+weight2 < maxW:
        return value1+value2
    else:
        weight1_greater_than_maxW = weight1>maxW
        weight2_greater_than_maxW = weight2>maxW
        if weight1_greater_than_maxW and weight2_greater_than_maxW:
            return 0
        elif weight1_greater_than_maxW:
            return value2
        elif weight2_greater_than_maxW:
            return value1
        else:
            return max(value1,value2)