def solution(k):
  r,y = [],[]
  m = 1

  while m <= k:
    if m % 2 == 0:
      r.append(m ** 2)
    else:
      y.append(m ** 2)

    m += 1

  return sum(r) - sum(y)