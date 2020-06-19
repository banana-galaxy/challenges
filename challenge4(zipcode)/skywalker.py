def validate(x):
    try:
        int(x)
    except:
        return False
    if x!=int(x):
        return False
    if not str(x).isdigit():
        return False
    if len(str(x))!=5:
        return False
    for i in range(4):
        if str(x)[i]==str(x)[i+1]:
            return False
    for i in range(3):
        if str(x)[i]==str(x)[i+2]:
            return False
    return True