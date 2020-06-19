def validate(x):
    xx = str(x)
    if xx.isnumeric() == True:
        if len(xx) == 5:
            if xx[0] != xx[1] and xx[1] != xx[2] and xx[2] != xx[3] and xx[3] != xx[4] and xx[0] != xx[2] and xx[1] != xx[3] and xx[2] != xx[4]:
                return True
            else:
                return False

        else:
            return False

    else:
        return False