def validate(code):
    str_code = str(code)
    if len(str_code) != 5 or not str_code.isdigit():
        return False
    for i in range(len(str_code)-1):
        if str_code[i] == str_code[i+1]:
            return False
        if i > 0 and str_code[i-1] == str_code[i+1]:
            return False
    return True