def lateRide(n: int) -> int:
    h = n // 60
    m = round(n / 60 % 1 * 60)

    return sum(list(map(int, list(str(h) + str(m)))))