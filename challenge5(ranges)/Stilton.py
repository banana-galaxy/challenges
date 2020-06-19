def erange(*args):
  result = []
  if len(args) == 1:
    stop, start, step = args[0]-1, 0, 1

    while start <= stop:
      result.append(start)
      start += step 

  elif len(args) == 3:
    start, stop, step = args[0], args[1], args[2]
    if step == 0:
      raise Exception("Step argument needs to be bigger than 0")
 
  elif len(args) == 2:
    start, stop, step = args[0], args[1], 1
    if not isinstance(stop, int) or not isinstance(start, int):
      raise Exception("Arguments need to be of type int") 
  
  else:
    raise Exception("The function only accepts a minimum of 1 arg or maximum of 3 args")

  if not isinstance(stop, int) or not isinstance(start, int) or not isinstance(step, int):
    raise Exception("Arguments need to be of type int")    

  if step < 0 and start > stop:
    while start > stop:
      result.append(start)
      start += step 
      
  elif step > 0:
    while start < stop:
      result.append(start)
      start += step 
  return result

def numerate(iterable, start=0):
  result = []
  for i in iterable:
    result.append((start, i))
    start += 1
  return result