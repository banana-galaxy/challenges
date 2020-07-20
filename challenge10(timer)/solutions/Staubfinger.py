def laterRide(n):
    assert type(n) == int, "int expected got something else!"
    h = 0

    while n >= 60:
        n -= 60
        h += 1

    ret = 0
    for i in str(h):
        ret += int(i)
    for i in str(n):
        ret += int(i)
    return ret