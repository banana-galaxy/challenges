def group(nr):
    return_list = []
    while nr != 0:
        return_list.append(nr % 100)
        nr //= 100
    return return_list
def nr_of_digits(nr):
    count = 0
    if nr == 0:
        return 1
    while nr != 0:
        count += 1
        nr //= 10
    return count
def sqrt_min(nr):
    if nr == 0:
        return 0
    elif nr >= 1 and nr < 4:
        return 1
    elif nr >= 4 and nr < 9:
        return 2
    elif nr >= 9 and nr < 16:
        return 3
    elif nr >= 16 and nr < 25:
        return 4
    elif nr >= 25 and nr < 36:
        return 5
    elif nr >= 36 and nr < 49:
        return 6
    elif nr >= 49 and nr < 64:
        return 7
    elif nr >= 64 and nr < 81:
        return 8
    elif nr >= 81 and nr < 100:
        return 9
def sqrt(number):
    return_value = sqrt_min(number[-1])
    if number[0] != number[-1]:
        rest = (number[-1] - return_value * return_value) * 100 + number[-2]
    else:
        rest = (number[-1] - return_value * return_value)
    number.pop(-1)
    while number != []:
        for i in range(9, -1, -1):
            some_value = (return_value * 2 * 10 + i) * i
            if  some_value <= rest:
                return_value = return_value * 10 + i
                rest = (rest - some_value) * 100 + number[-1]
                number.pop(-1)
                break
    return rest
def solution(nr):
    if nr > 1:
        var = sqrt(group(nr))
        if var == 0:
            return True
    return False