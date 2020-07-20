def lateRide(n):
    hours = []
    time = 0
    division, remainder  = str((n // 60)), str((n % 60))

    for x in range(len(division)):
        #hours.append(int(division[x])) Gives you the divison
        time += int(division[x])
    for y in range(len(remainder)):
        #hours.append(int(remainder[y])) Gives you the remainder
        time += int(remainder[y])
    #return hour Gives you the time, like in the example: 13:28 = [1, 3, 2, 8]
    return time # Gives you the actual time