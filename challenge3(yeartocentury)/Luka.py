def yearToCentury(year):
    century=1
    year=str(year)
    length=len(year)
    if length>=3:
        century=year[0:(length-2)]
        century=int(century)
        if (int(year[length-1])!=0 or int(year[length-2])!=0):
            century+=1
    return century

if __name__ == "__main__":
    print(yearToCentury(600))
    print(yearToCentury(0))
    print(yearToCentury(599))
    print(yearToCentury(601))
    print(yearToCentury(1412))