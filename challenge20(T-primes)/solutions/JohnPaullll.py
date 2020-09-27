def solution(num):
    if num < 4: return False
    i = (num ** 0.5)
    if not i.is_integer():
        return False
    j = int(i ** 0.5)
    while not (i / j).is_integer():
        j -= 1
    return j == 1