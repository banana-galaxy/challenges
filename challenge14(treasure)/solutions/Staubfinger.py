def solution(value1: int, weight1: int, value2: int, weight2: int, mawweight)-> int:
    if mawweight < (weight1 + weight2):
        return value1 + value2
    elif value1 >= value2:
        if weight1 < mawweight:
            return value1
        elif weight2 < mawweight:
            return value2
    elif value2 > value1:
        if weight2 < mawweight:
            return value2
        elif weight1 < mawweight:
            return value1
    return 0