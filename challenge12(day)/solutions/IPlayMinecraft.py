def solution(weekday, date, qdate):
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    difference = 0
    d1, m1 = map(int, date.split("/"))
    d2, m2 = map(int, qdate.split("/"))
    wd = weekdays.index(weekday.lower())
    difference += max(d1, d2) - min(d1, d2)
    difference += (max(m1, m2) - min(m1, m2)) * 30
    return weekdays[(wd + difference) % 7].title()