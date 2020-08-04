def solution(day_then,date_then,date_now) :
    day_names = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    day_then = day_then.lower()
    # Asuming that there are 30 days in every month
    f = lambda x : (int(x[3:].lstrip("0"))*30) + int(x[:2].lstrip("0"))
    days = (f(date_now) - f(date_then))
    n = 0
    while 1 :
        if (days-n)%7 == 0 :
            n = days-n
            break
        else :
            n+=1
    plus = days-n
    if plus > (6-day_names.index(day_then)) :
        plus =  days-n-7
    return day_names[ day_names.index(day_then) + plus ]