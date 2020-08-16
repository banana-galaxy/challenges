def solution(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 > maxW:
        if value1 >= value2 and maxW >= weight1:
            return value1
        elif maxW >= weight2:
            return value2
        else:
            return None
    else:
        return value1 + value2