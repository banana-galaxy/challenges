def lateRide(n):
    n = int(n)
    hours = str(n // 60)
    minutes = str(n % 60)
    lstHours = [x for x in hours]
    lstMins = [x for x in minutes]
    lstTime = []
    for x in lstMins:
        lstTime.append(int(x))
    for x in lstHours:
        lstTime.append(int(x))
    print(lstTime)
    total = 0
    for e in range(0, len(lstTime)):
        total += lstTime[e]
    print(total)