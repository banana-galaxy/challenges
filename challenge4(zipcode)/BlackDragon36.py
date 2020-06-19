def validate(code):
    if code.isdigit() and len(code) == 5:
        for i in range(0, 3):
            if code[i] == code[i + 2]:
                return False
        return True
    else:
        return False