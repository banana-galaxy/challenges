def lateRide(a):
    return sum(int(x) for x in str(a // 60 % 24)) + sum(int(y) for y in str(a % 60))