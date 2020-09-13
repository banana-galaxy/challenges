def solution(direction):
    compass = {
            'n': 1,
            's': -1,
            'e': 1,
            'w': -1
    }
    if len(direction) > 10:
        return False
    else:
        x_axis = 0
        y_axis = 0

        for move in direction:
            if move in ['n', 's']:
                x_axis += compass[move]
            else:
                y_axis += compass[move]
        if x_axis == y_axis == 0:   return True
        else:   return False