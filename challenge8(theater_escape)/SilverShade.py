def whichExit(theatre):
    # Get my Row and Seat
    for row in theatre:
        if 0 in row:
            myrow = row
            myseat = row.index(0)
            break

    # Get people sitting/unoccupied on the left hand side
    leftside = []
    for person in myrow:
        if person != 0:
            leftside.append(person)
        else:
            break

    # Get people sitting/unoccupied on the right hand side
    rightside = []
    for person in myrow[myseat + 1:]:
        rightside.append(person)

    # returns output based on the number of people sitting on either sides
    if leftside.count(1) > rightside.count(1):
        return 'right'
    elif leftside.count(1) < rightside.count(1):
        return 'left'
    else:
        return 'same'