def lateRide(n):
  return sum([int(x) for x in str(n%60)+str(n//60)])