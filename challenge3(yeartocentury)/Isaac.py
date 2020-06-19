def yearToCentury(year):
    tmp = year/100
    if not tmp.is_integer():
        century = int(tmp) + 1
    else:
        century = int(tmp)    
    return century