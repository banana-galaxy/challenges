def incraseIntegers(input):
  input_copied = input
  to_return = 0
  index = 1
  while(True):
    if input_copied[index] <= input_copied[index - 1]:
      input_copied[index] += 1
      to_return += 1
    else:
      index += 1
    if index == len(input_copied):
      break
  return to_return