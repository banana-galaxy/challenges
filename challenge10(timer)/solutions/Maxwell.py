def lateRide(n):
    h = n // 60
    m = n % 60
    return(sum([int(x) for x in str(h)+str(m)]))