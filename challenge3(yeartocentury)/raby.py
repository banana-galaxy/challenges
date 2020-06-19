def yearToCentury(year):

    century = 0
    
    for i in range(1, year + 1):
        century += 1

    return round(century / 100)