def solution(day, date1, date2):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday","saturday","sunday"]
    day = days.index(day.lower())

    date1 = (int(date1[0:2]), int(date1[3:5]))
    date2 = (int(date2[0:2]), int(date2[3:5]))
    duration = abs(date1[0] - date2[0]) + 30*(abs(date1[1]-date2[1]))
    return days[(day + (duration % 7)) % 7]