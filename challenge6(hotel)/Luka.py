def matrixSum(hotel):
    cost=0
    for floorNumber,floor in enumerate(hotel):
        for roomNumber, room in enumerate(floor):
            summ=True
            for i in range(floorNumber):
                if hotel[i][roomNumber]==0:summ=False
            if summ:cost+=room
    return cost