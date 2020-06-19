def validate(code):
    try:
        float(code)
    except ValueError:
        return False
    else:
        if not float(code).is_integer():
            return False
    code = str(code)
    if len(code) != 5:
        return False
    for x in range(3):
        if code[x] == code[x+2]:
            return False
    for x in range(4):
        if code[x] == code[x+1]:
            return False
    return True