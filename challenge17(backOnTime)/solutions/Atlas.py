def solution(directions):
    if len(directions) > 10:
        return False
    lat = 0
    long = 0
    for direction in directions:
        if direction == "n":
            lat += 1
        elif direction == "s":
            lat -= 1
        elif direction == "e":
            long += 1
        else:
            long -= 1
    if lat == 0 and long == 0:
        return True
    return False