def validate(zipCode):
    if isinstance(zipCode,int) and len(str(zipCode)) == 5:
        s = str(zipCode)
        temp = [a for a, b in zip(s, s[2:]) if a == b]
        if len(temp) == 0:
            return True
        else:
            return False
    else:
        return False