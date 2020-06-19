def validate (num):
    result = True
    global y
    y = int(0)
    #checking if not int
    if str(num.__class__) != "<class 'int'>":
        result = False
    
    #creating list
    global digits
    digits = []
    digits = [int(x) for x in str(num)]

    #checking for right len
    if len(digits) != 5:
        result = False

    
    #checking for repetitive or neighboring digits in list
    if result == True:
        for x in range (0,3):
            if digits[x] == digits[x+2]:
                result = False
        for x in range(0,4):
            if digits[x] == digits[x+1]:
               result = False   
    #returning result   
    return (result)