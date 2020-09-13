def solution(directions):
    if len(directions) > 10:
        return False
    else:
        x = 0
        y = 0
        for direction in directions:
            if direction.lower() == "e":
                x += 1
            elif direction.lower() == "w":
                x -= 1
            elif direction.lower() == "n":
                y += 1
            elif direction.lower() == "s":
                y -= 1
        if x == 0 and y == 0:
            return True
        else:
            return False