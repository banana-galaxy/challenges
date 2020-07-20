def lateRide(n):
    hour = n//60
    minute = n%60
    result = list(map(int,str(hour)+str(minute)))
    return sum(result)