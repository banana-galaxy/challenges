def yearToCentury(year: int):
    if year%100 == 0:
        century = year//100
    else:
        century = year//100 + 1
        
    century = int(century)
    
    return century