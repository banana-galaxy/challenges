def yearToCentury(year):
    i = int(year)
    c = i//100
    if i % 100:
        c += 1
    print(c)