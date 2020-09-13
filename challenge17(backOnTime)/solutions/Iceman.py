def solution(directions: list) -> bool:
    cords: list = [0, 0]
    cord_update: dict = {
        'n': lambda cords: [cords[0], cords[1]+1],
        'e': lambda cords: [cords[0]+1, cords[1]],
        's': lambda cords: [cords[0], cords[1]-1],
        'w': lambda cords: [cords[0]-1, cords[1]],
    }  # this whole dict is 1 lines of code ?
    for direction in directions:
        cords = cord_update[direction](cords)
    return True if cords==[0, 0] else False