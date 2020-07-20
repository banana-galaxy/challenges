def lateRide(time):
    try:
        a = time // 600
        b = (time - a * 600) // 60
        c = (time - a * 600 - b * 60) // 10
        d = time - a * 600 - b * 60 - c * 10

        # if time is greater or equal 24h
        while (a >= 2 and b >= 4) or a >= 3:
            a -= 2
            b -= 4
            if b < 0:
                a -= 1
                b += 10
        return a + b + c + d
    # if invalid input
    except TypeError:
        return "Invalid input!"