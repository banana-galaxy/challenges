def lateride(n):
    hour_list = []
    minute_list = []
    hour = n//60
    minute = n - 60*hour
    hour = str(hour)
    minute =  str(minute)
    for digits in hour:
        hour_list.append(digits)
    for digits in minute:
        minute_list.append(digits)
    if len(hour_list) == 1:
        hour = f'0{hour}'
    if len(minute_list) == 1:
        minute = f'0{minute}'
    hour = sum(list(map(int, hour)))
    minute = sum(list(map(int, minute)))
    return hour + minute