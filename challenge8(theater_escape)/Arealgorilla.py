def whichExit(seats):
    right, left = 0, 0
    me = list(*[(row, coloumn) for row in range(len(seats)) for coloumn in range(len(seats[row])) if
                seats[row][coloumn] == 0])

    for num in range(len(seats[me[0]])):
        if seats[me[0]][num] != -1:
            if num < me[1]:
                left += 1
            if num > me[1]:
                right += 1

    if left < right:
        return 'left'
    elif left > right:
        return 'right'
    else:
        return 'same'