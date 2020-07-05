def which_exit(seat_format):
    # vars
    pos1, pos2, right, left, zero = 0, 0, 0, 0, False
    # checking for 0
    for n in range(len(seat_format)):
        for i in range(len(seat_format[0])):
            if seat_format[n][i] == 0:
                zero = True
                pos2 = i + 1
                break
        if zero:
            pos1 = n + 1
            break
    # checking right
    for n in range(pos1):
        for i in range(pos2):
            if seat_format[n][i] == 1:
                right += 1
    # checking left
    for n in range(pos1):
        for i in range(pos2 - 1, len(seat_format[0])):
            if seat_format[n][i] == 1:
                left += 1
    # comparing the right from the left
    if right > left:
        return 'left!'

    if right < left:
        return 'right!'

    if right == left:
        return 'same!'