def solution(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    elif value2 > value1:
        if weight2 < maxW:
            return value2
        else:
            return value1
    else:
        if weight1 < maxW:
            return value1
        else:
            return value2
    return 0