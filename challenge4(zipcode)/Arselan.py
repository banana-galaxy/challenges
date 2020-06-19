def validate(zipCode):
    if isinstance(zipCode, int):
        count = len(str(zipCode))
        strZip = str(zipCode)
        if count == 5:
            if strZip[0] == strZip[1]:
                return False
            if strZip[0] == strZip[2]:
                return False
            if strZip[1] == strZip[2]:
                return False
            if strZip[1] == strZip[3]:
                return False
            if strZip[2] == strZip[3]:
                return False
            if strZip[2] == strZip[4]:
                return False
            if strZip[3] == strZip[4]:
                return False
            else:
                return True
        else:
            return False
    else:
        return False