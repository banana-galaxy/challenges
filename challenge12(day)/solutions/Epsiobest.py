def solution(day,f_date,s_date):
    d,m = f_date.split("/")
    d2,m2 = s_date.split("/")
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    index = days.index(day.lower())
    d,d2,m,m2 = int(d),int(d2),int(m),int(m2)
    while d != d2 or m != m2:
        if m == m2:
            if d2 > d:
                index += 1
                d += 1
            else:
                index -= 1
                d -= 1
        elif m2 > m:
            if d <= 30:
                d += 1
                index += 1
            elif d > 30:
                d = 1
                m += 1
        elif m2 < m:
            if d >= 1:
                d -= 1
                index -= 1
            elif d < 1:
                d = 30
                m -= 1
        if index < 0:
            index = 6
        if index > 6:
            index = 0

    return days[index]