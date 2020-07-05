def matrixSum(matrix):
    addlist = []
    currentfloor = 0
    for floor in matrix:
        currentfloor += 1
        for room in floor:
            roomind = floor.index(room)
            if room > 0 and currentfloor > 1:
                roomsabove = []
                for fl in range(1, currentfloor):
                    roomsabove.append(matrix[fl - 1][roomind])
                if 0 not in roomsabove:
                    addlist.append(room)
                else:
                    pass
            elif room > 0 and currentfloor <= 1:
                addlist.append(room)
            else:
                pass
    roomprice = 0
    for roomp in addlist:
        roomprice += roomp
    return roomprice