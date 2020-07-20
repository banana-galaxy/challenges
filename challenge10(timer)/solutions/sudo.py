def lateRide(n):
    # get the hours in impropper fraction
    a = n / 60
    # round to get the hour hours
    hours = round(a-0.5)
    # find the minutes
    minutes = round((a - hours)*60)
    # get the answer
    Sum = 0
    hours = str(hours)
    minutes = str(minutes)
    a = hours + minutes
    a = int(a)
    while(a > 0):
        Reminder = a % 10
        Sum = Sum + Reminder
        a = a //10
    #returns the answer
    return Sum