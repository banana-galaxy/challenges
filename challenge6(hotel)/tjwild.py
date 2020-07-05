def matrixSum(matrix):

    output = 0
    haunted_col = []

    #Goes through each floor
    for q in enumerate(matrix):

        #Goes through each floor on the room
        for i in enumerate(q[1]):

            #Only deals with it if it's column hasn't been labeled as 'haunted'
            if(i[0] not in haunted_col):

                #If room haunted, add that column to list of haunted columns (all rooms beneath)
                if(i[1] == 0):
                    haunted_col.append(i[0])
                #Else, add value of that room to the sum output
                else:
                    output += i[1]

    return output