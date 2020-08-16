def solution(value1: int, weight1: int, value2: int, weight2: int, maxW: int):
    if maxW >= weight1 + weight2:
        return value1 + value2
    elif maxW <= weight2 and weight1 <= maxW:
        return value1
    elif weight2 <= maxW and maxW <= weight1:
        return value2
    elif maxW >= weight1 and maxW >= weight2 and value1 >= value2:
        return value1
    elif maxW >= weight1 and maxW >= weight2 and value1 <= value2:
        return value2
    else:
        return 0