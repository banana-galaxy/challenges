def lateRide(n):
    output = 0
    mins = n % 60
    hrs = int((n / 60) - ((n % 60) / 60))

    if hrs < 10:
        output += hrs
    else:
        for digit in str(hrs):
            output += int(digit)

    if mins < 10:
        output += mins
    else:
        for digit in str(mins):
            output += int(digit)

    return output