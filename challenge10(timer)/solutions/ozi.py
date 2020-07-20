def lateRide(n: int):  # n is the time in minutes that has passed

    # assuming the longest time the rider has been out is less than 24 hours
    hour = n // 60
    minute = n % 60

    time = str(hour) + str(minute)
    sum_of_digits = 0
    for digit in time:
        sum_of_digits += digit

    return sum_of_digits