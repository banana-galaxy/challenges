def validate(z_code):
    z_code = z_code.replace(" ", "")
    for i in range(1,6,2):
        if not z_code[i].isdigit():
            return False
    for i in range(0,5,2):
        if not z_code[i].isalpha():
           return False
    return z_code.upper()