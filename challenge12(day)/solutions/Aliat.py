def solution(day, date_1, date_2):
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    x = week.index(day)
    day_1 = (int(date_1.split("/")[1])-1) * 30 + int(date_1.split("/")[0])
    day_2 = (int(date_2.split("/")[1])-1) * 30 + int(date_2.split("/")[0])
    while day_1 < day_2:
        day_1 += 1
        x += 1
        if x == 7:
            x = 0
    while day_2 < day_1:
        day_1 -= 1
        x -= 1
        if x == -1:
            x = 6
    return week[x]