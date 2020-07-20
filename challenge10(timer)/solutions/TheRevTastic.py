def lateRide(n):
    time = '{:02d}{:02d}'.format(*divmod(n, 60))

    time_list = [int(num) for num in time]

    return int(sum(time_list))