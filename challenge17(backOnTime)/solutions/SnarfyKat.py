def solution(directions):

    if len(directions) > 10:
        return False

    starting_location = {'x': 0, 'y': 0}
    location = starting_location.copy()

    for direction in directions:
        if direction == 'n':
            location['y'] += 1
        elif direction == 's':
            location['y'] -= 1
        elif direction == 'w':
            location['x'] -= 1
        elif direction == 'e':
            location['x'] += 1

    return location == starting_location