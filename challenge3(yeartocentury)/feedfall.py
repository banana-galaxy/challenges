def yearToCentury(baseint:int=1,mode=int):
    if mode == int: #make a int output
        return round(baseint/100) #return the integer century
    elif mode==float: #make a float output
        return baseint/100 #return the century in float
    else:
        raise TypeError(f"mode data types can only be int or float! not {mode}") #raises an error if a invalid data type is inputted