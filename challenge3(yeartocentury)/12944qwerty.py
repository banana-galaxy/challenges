def yearToCentury(year):
    century = round(year/100)*100
    if century <= year:
        century = century/100 + 1
    else:
        century = century/100
    return int(century)