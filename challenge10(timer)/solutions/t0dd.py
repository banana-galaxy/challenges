def lateRide(x):
    t=''.join((str(x*60//3600), str(x*60//60-(x*60//3600)*60)))
    return (sum([int(n) for n in t]))