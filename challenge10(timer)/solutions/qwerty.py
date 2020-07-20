def lateRide(n):
    hours, minutes = [str(i) for i in divmod(n, 60)]
    out = 0
    for i in hours: out += int(i)
    for i in minutes: out += int(i)
    return out