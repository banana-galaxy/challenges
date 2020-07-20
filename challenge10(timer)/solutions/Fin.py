def lateRide(n):
    h, m = divmod(n, 60)
    r = h, m
    return ':'.join(map('{:02d}'.format, r))