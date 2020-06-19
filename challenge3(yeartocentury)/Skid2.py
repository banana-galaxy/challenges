def yearToCentury(year):
    year = int(year)
    if year < 1:
        return "Please try again with a valid year"
    year = list(str(year))
    if len(year)>2:
        if int(year[-1])>0 or int(year[-2])>0:
            del year[-2:]
            i = ""
            century = int(i.join(year))+1
            return century
        else:
            del year[-2:]
            i = ""
            century = int(i.join(year))
            return century
    else:
        century = 1
        return century