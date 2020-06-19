def yearToCentury(year):
    a = 0
    year = str(year)
    for i in year:
        a += 1
    if a == 4:
        if year[-1] != "0":
            zh = int(year[0]+"0")
            en = int(year[1])+1
            return zh+en
        elif year[-2] != "0":
            zh = int(year[0]+"0")
            en = int(year[1])+1
            return zh+en
        else:
            res = year[0]+year[1]
            return res
    elif a == 3:
        if year[-1] != "0":
            zh = int(year[0])+1
            return zh
        elif year[-2] != "0":
            zh = int(year[0])+1
            return zh
        else:
            return year[0]