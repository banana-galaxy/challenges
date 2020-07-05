def whichExit(x):
  countl = 0
  countr = 0
  y = []
  for i in x:
    for j in i:
      if j == 0:
        y.append(i)

  for i in y:
    for j in i:
      if j == 0:
        break
      elif j == 1:
        countl += 1

  for i in y:
    for j in i:
      if j == 0:
        countr = 0
      elif j == 1:
        countr += 1

  if countl > countr:
    return "right"
  elif countl == countr:
    return "same"
  else:
    return "left"