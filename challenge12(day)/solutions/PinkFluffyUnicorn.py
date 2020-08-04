def solution(day,date1,date2):
    x = ((int(date2.split("/")[1]) - int(date1.split("/")[1]))*30)-((int(date2.split("/")[0]) - int(date1.split("/")[0]))*(-1))
    list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    if x < 0:
        x = x*(-1)
        list.reverse()
    return [list[j%len(list)] for j in range(list.index(day.lower())+1, list.index(day.lower())+1+x)][-1]