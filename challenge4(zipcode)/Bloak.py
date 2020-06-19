def validate(code):
    if type(code) == int:
        code = str(code)
    if type(code) == str:
        if not code.isdigit():
            return False
        elif len(code) != 5:
            return False
        else:
            for index in range(len(code)):
                if index + 1 < len(code):
                    if code[index + 1] == code[index]:
                        return False
                if index + 2 < len(code):
                    if code[index + 2] == code[index]:
                        return False
            return True
    else:
        return False