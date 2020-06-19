def validate(num): #num is a string e.g.'12345'
    #check if is int
    try:
        int(num)
    except:
        return False
    #check if 5 digits
    if len(num) != 5:
        return False
    #check neighbor numbers
    for x in range(3):
        for i in range(10):
            if num[x:x+3].count(str(i)) >= 2:
                return False
    return True