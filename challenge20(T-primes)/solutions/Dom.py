def solution(x: int) -> bool:
    r = x**0.5
    if r.is_integer():
        if r <= 3:
            return r > 1
        elif (r % 2 == 0) | (r % 3 == 0):
            return 0

        for i in range(5, int(r**0.5)+1, 2):
            if r % i == 0:
                return 0
        return 1
    return 0