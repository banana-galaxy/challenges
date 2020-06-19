def validate(code):
    #Checking if it's made of only integers
    try:
        int(code)
    except ValueError:
        return False

    #Checking if there are only 5 integers total, no less no more
    if len(str(code)) != 5:
        return False

    #Checking if there are no alternating repetitive digits
    for i in range(4): 
        if i == 3: #The second last digit only has to be checked only with digit right next to it ie. the last digit
            if str(code)[i] == str(code)[i+1]:
                return False
        else: #All the others have to be checked with the digit right next to it, as well as 2 places forward if it
            if str(code)[i] == str(code)[i+1] or str(code)[i] == str(code)[i+2]:
                return False

    return True