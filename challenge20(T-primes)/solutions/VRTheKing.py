def solution(n):
  a = n ** 0.5
  if a.is_integer():
    if a <= 3:
      return a > 1
    elif a % 2 == 0 or a % 3 == 0:
      return False
    i = 5
    while i * i <= a:
      if a % i == 0 or a % (i + 2) == 0:
        return False
      else:
        i = i + 6
    return True
  else:
      return False