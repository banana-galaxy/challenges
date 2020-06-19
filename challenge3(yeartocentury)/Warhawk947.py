def yearToCentury(y):
  y = str(y) # Convert into string 

  if len(y) <= 2: # If the year is less than 2 digits, it's part of century one
    return 1
  if int(y[-2:]) == 00:
    return int(y[:-2])
  else:
    return int(y[:-2]) + 1 # Take everything except the last 2 digits, add one, and we're done!