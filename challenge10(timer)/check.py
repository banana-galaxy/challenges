'''def lateRide(n):
    return sum(map(int, str(n // 60) + str(n % 60)))'''

def lateRide(n):
    return n//60%10+n%60%10+n//600+n%60//10