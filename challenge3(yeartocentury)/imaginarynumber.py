def yearToCentury(year):
  try:
    year = int(year)
    r = round(year, -2)
    re = r / 100
    if year > r:
      return int(re + 1)
    else: return re


  except:
    print("Not a valid integer.")