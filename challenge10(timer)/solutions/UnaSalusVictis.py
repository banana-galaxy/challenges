def lateRide(minutes):
    return sum([int(i) for i in str(divmod(minutes, 60)) if i.isnumeric()])