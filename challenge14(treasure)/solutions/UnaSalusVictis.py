def solution(value1: int, weight1: int, value2: int, weight2: int, maxWeight: int):
    # both weights are too great
    if weight1 > maxWeight and weight2 > maxWeight:
        return 0

    # both weight are enough to carry
    elif weight1 + weight2 <= maxWeight:
        return value1 + value2

    # either weight is too heavy to carry
    elif weight1 > maxWeight:
        return value2
    elif weight2 > maxWeight:
        return value1

    # greatest value
    elif value1 >= value2:
        return value1
    elif weight2 <= maxWeight:
        return value2

    # did I miss something?
    else:
        return ":shrug:"