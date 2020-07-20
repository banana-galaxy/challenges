def lateRide(n):
    mins = n % 60
    hrs = (n - mins) / 60
    time_str = str(int(hrs)) + str(int(mins))
    result = 0
    result += [num for num in time_str]
    return result