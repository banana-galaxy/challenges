def lateRide(time):
    hours = int(time / 60)
    minutes = time - (60 * hours)

    hours_array = list(str(hours))
    minutes_array = list(str(minutes))

    count = 0
    for i in range(len(hours_array)):
        count += int(hours_array[i])
    
    for i in range(len(minutes_array)):
        count += int(minutes_array[i])
    
    return count