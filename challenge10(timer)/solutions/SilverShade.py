def lateRide(n, re=0):
    for d in f'{n//60}{n%60}':
        re += int(d)
    return re