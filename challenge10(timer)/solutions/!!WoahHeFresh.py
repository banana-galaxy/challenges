def lateRide(n):
    time = str(n//60) + str(n%60)
    ans = 0
    for char in time: ans = ans + int(char)
    return ans