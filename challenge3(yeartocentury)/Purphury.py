def yearToCentury(year):
    # alternative method with an import
    # from math import ceil
    # return ceil(year/100)
    
    century = year // 100
    
    if year % 100:
        century += 1
    
    return century