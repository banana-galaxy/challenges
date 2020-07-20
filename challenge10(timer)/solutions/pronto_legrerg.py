def lateRide(minutes: int) -> int:
    hours = int(minutes/60)
    minutes = minutes % 60
    total = 0
    for char in str(hours) + str(minutes):
        total += int(char)
    return total