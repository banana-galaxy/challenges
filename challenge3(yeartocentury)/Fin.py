def yearToCentury(year):
    if year % 100 == 0:
        return int(year / 100)
    else:
        return int(round(year // 100) + 1)