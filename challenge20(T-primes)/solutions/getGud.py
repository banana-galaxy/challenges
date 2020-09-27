def solution(num):
  if num == 1:
    return 0
  elif (s1 := num**0.5)%1 == 0:
    if s1 in [2, 3, 5, 7]:
      return 1
    elif s1%3 == 0:
      return 0
    elif s1%5 == 0:
      return 0
    elif s1%7 == 0:
      return 0
    else:
      return 1
  else:
    return 0