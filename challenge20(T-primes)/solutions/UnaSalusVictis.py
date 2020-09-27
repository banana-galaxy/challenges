def solution(number: int):
    if number < 4:
        return False
    elif number == 4:
        return True
    elif number % 2 == 0:
        return False

    sq = number ** 0.5
    if sq != int(sq):
        return False

    for x in range(3, int(sq ** 0.5) + 1, 2):
        if sq % x == 0:
            return False

    return True