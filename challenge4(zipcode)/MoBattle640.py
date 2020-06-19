def validate(code):
  # Assuming a string is passed in, not an int 
  try:
    if float(code) != int(code):
      return False 
  except:
    return False
  if len(code) != 5:
    return False 
  for i in range(4):
    if code[i] == code[i+1]:
      return False 
  return True