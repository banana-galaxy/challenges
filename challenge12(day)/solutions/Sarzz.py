def solution(day, date1, date2):
    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    date1 = date1.split("/")
    date2 = date2.split("/")
    ans = int(date2[0]) - int(date1[0])
    if date1[1] != date2[1]:
        n = int(date2[1]) - int(date1[1])
        ans += 30 * n
    x = days.index(day.lower())
    for i in range(abs(ans)):
        if abs(ans) + x < len(days):
            return days[x + ans]
        elif ans > 0:
            ans = ans - 7
        else:
            ans = ans + 7
    #return days[ans]


print(solution('monday', '14/05', '12/10'))