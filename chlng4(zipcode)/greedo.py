def verify(zipcode):
    if not isinstance(zipcode, int):
        return False
    zipstring = str(zipcode)
    if not len(zipstring) == 5:
        return False
    for i in range(len(zipstring)):
        if not i == 4:
            if zipstring[i] == zipstring[i+1]:
                return False
            if not i == 3:
                if zipstring[i] == zipstring[i+2]:
                    return False
    return True