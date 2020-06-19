def yearToCentury(year):
    century = divmod(year,100)
    if century[1] != 0:
       return century[0] + 1
    else:
      return century[0]