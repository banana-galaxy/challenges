def whichExit(theater):
    for row in theater:
        if 0 in row:
            left = 0
            right = 0
            side = 'left'
            for person in row:
                if person == 1 and side == 'left':
                    left += 1
                elif person == 1 and side == 'right':
                    right += 1
                elif person == 0 and side == 'left':
                    side = 'right'

            if left > right:
                return 'right'
            elif right > left:
                return 'left'
            else:
                return 'same'
            break