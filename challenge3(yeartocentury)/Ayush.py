def yearToCentury(year):
    if 1<=year<100:
        century = 1
    else:
        century = round(year/100)
    return century